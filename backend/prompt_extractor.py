from rake_nltk import Rake
import nltk


class PromptExtractor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def extract_prompt(self, text: str) -> str:
        print("input: ", text)
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()[0]
        print(keyword_extracted)
        return keyword_extracted + " oil painting"
