from typing import Dict

from rake_nltk import Rake
import nltk
import yake


class PromptExtractor:
    def __init__(self, style: str = "oil painting"):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.style = style

    def _extract_prompt_with_nltk(self, text: str) -> str:

        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()[0]
        prompt = keyword_extracted
        return prompt

    def _extract_prompt_with_yake(self, text: str) -> str:
        kw_extractor = yake.KeywordExtractor(n=5, dedupLim=0.9, top=2, features=None)
        extracted_words = " ".join(
            [kw_extractor.extract_keywords(text)[0][0], kw_extractor.extract_keywords(text)[1][0]])
        return extracted_words

    def extract_paragraphs_with_prompts(self, whole_text: str) -> Dict[str, str]:
        print(whole_text)
        paragraph_prompts = {}
        paragraph = ""
        sentence_counter = 0
        lines = whole_text.splitlines()
        non_empty_lines = " ".join([line for line in lines if line.strip() != ""])
        for idx, sentence in enumerate(non_empty_lines.split(".")):
            sentence_counter += 1
            paragraph += sentence.strip()
            if sentence_counter == 5:
                sentence_counter = 0
                print("input: ", paragraph)
                extracted_keywords = self._extract_prompt_with_yake(
                    paragraph) + " " + self._extract_prompt_with_nltk(paragraph)

                words = extracted_keywords.lower().split()
                deduplicated_prompt = " ".join(sorted(set(words), key=words.index))
                print("extracted: ", deduplicated_prompt)
                paragraph_prompts[paragraph] = deduplicated_prompt
                paragraph = ""
        return paragraph_prompts
