from typing import Dict

from rake_nltk import Rake
import nltk
import yake


class PromptExtractor:
    def __init__(self, style: str = "oil painting"):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.style = style

    def _extract_prompt(self, text: str) -> str:
        print("input: ", text)
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()[0]
        prompt = keyword_extracted + " " + self.style
        return prompt

    def _extract_prompt_with_yake(self, text: str) -> str:
        print("input: ", text)
        kw_extractor = yake.KeywordExtractor(n=3, dedupLim=0.9, top=3, features=None)
        extracted_words = " ".join([kw_extractor.extract_keywords(text)[0][0], kw_extractor.extract_keywords(text)[1][0]])
        print("extracted:", extracted_words)
        return extracted_words + " " + self.style

    def extract_paragraphs_with_prompts(self, whole_text: str) -> Dict[str, str]:
        paragraph_prompts = {}
        paragraph = ""
        line_with_content_counter = 0
        for idx, line in enumerate(whole_text.splitlines()):
            if line.strip():
                line_with_content_counter += 1
                paragraph += line
            if line_with_content_counter == 3:
                line_with_content_counter = 0
                paragraph_prompts[paragraph] = self._extract_prompt_with_yake(paragraph)
                paragraph = ""
        return paragraph_prompts
