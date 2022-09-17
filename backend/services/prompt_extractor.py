import numpy as np
from rake_nltk import Rake
import nltk
import yake
from transformers import pipeline
from filecache import filecache

class PromptExtractor:
    MAX_SENTENCE_COUNT = 10
    MIN_SENTENCE_COUNT = 5

    def __init__(self, style: str = "oil painting"):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.overall_extractor = yake.KeywordExtractor(n=1, dedupLim=0.5, top=20, features=None)
        self.style = style


    @staticmethod
    @filecache(24 * 60 * 60)
    def _extract_prompt_with_nltk(text: str) -> str:
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()[0] + rake_nltk_var.get_ranked_phrases()[1]
        prompt = keyword_extracted
        return prompt

    @staticmethod
    @filecache(24 * 60 * 60)
    def _extract_prompt_with_yake(text: str) -> str:
        kw_extractor = yake.KeywordExtractor(n=3, dedupLim=0.1, top=2, features=None)
        extracted_words = " ".join(
            [kw_extractor.extract_keywords(text)[0][0], kw_extractor.extract_keywords(text)[1][0]])
        return extracted_words


    @staticmethod
    @filecache(24 * 60 * 60)
    def _extract_prompt_with_bart(text: str) -> str:
        summarizer = pipeline("summarization", model="facebook/bart-large-xsum")
        return summarizer(text, min_length=5)[0]["summary_text"]

    @staticmethod
    @filecache(24 * 60 * 60)
    def _extract_prompt_with_bart_extended(text: str) -> str:
        kw_extractor = yake.KeywordExtractor(n=10, dedupLim=0.8, top=1, features=None)
        return kw_extractor.extract_keywords(PromptExtractor._extract_prompt_with_bart(text))[0][0]

    def _keywords_relevant_overall(self, extracted_keywords: str, whole_text_keywords):
        overall_important_keywords = np.array(whole_text_keywords)[:, 0]
        importance = 0
        for keyword in extracted_keywords.split(" "):
            if keyword in overall_important_keywords:
                importance += 1
        print("importance", importance, "for", extracted_keywords)
        return importance > 2

    def extract_paragraphs_with_prompts(self, whole_text: str):
        paragraph_prompts = {}
        paragraph = []
        sentence_counter = 0
        lines = whole_text.splitlines()

        whole_text_keywords = self.overall_extractor.extract_keywords(whole_text)
        print("overall keywords", whole_text_keywords)

        non_empty_lines = " ".join([line for line in lines if line.strip() != ""])
        for idx, sentence in enumerate(non_empty_lines.split(".")):
            sentence_counter += 1
            paragraph.append(sentence)
            if sentence_counter >= PromptExtractor.MIN_SENTENCE_COUNT:
                extracted_keywords = self.extract_keywords(" ".join(paragraph))

                if self._keywords_relevant_overall(extracted_keywords,
                                                   whole_text_keywords) or sentence_counter > PromptExtractor.MAX_SENTENCE_COUNT:
                    self.add_keywords_to_paragraph_prompts(extracted_keywords, " ".join(paragraph), paragraph_prompts)
                    sentence_counter = 0
                    paragraph = []
        return paragraph_prompts

    def extract_keywords(self, paragraph):
        extracted_keywords = self._extract_prompt_with_bart_extended(paragraph)
        return extracted_keywords

    def add_keywords_to_paragraph_prompts(self, extracted_keywords, paragraph, paragraph_prompts):
        print("input: ", paragraph)
        words = extracted_keywords.lower().split()
        deduplicated_prompt = " ".join(sorted(set(words), key=words.index))
        print("extracted: ", deduplicated_prompt)
        paragraph_prompts[paragraph] = deduplicated_prompt + " " + self.style

