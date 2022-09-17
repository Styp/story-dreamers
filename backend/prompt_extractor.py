from typing import Dict

from rake_nltk import Rake
import nltk


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
                paragraph_prompts[paragraph] = self._extract_prompt(paragraph)
                paragraph = ""
        return paragraph_prompts
