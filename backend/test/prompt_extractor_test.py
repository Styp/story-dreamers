import unittest
from os import path

from services.prompt_extractor import PromptExtractor


class MyTestCase(unittest.TestCase):

    def test_relevant_story_keyword_extraction(self):
        file_to_test = "snowwhite-test.txt"
        prompt_extractor = PromptExtractor()
        result = {}
        with open((path.join("test-data", file_to_test))) as story_file:
            result = prompt_extractor.extract_paragraphs_with_prompts(story_file.read())

        all_prompts = " ".join(str(x) for x in result.values()).lower()
        print(all_prompts)
        relevant_story_words = ["princess", "queen", "woods", "castle", "cottage", "bed"]
        missing_words = 0
        for word in relevant_story_words:
            if word not in all_prompts:
                print(f"Word {word} was missing in prompts")
                missing_words += 1

        accurracy = 100 - (100 / len(relevant_story_words) * missing_words)
        print("missing words", missing_words, "of", len(relevant_story_words))
        self.assertGreater(accurracy, 80)

        if __name__ == '__main__':
            unittest.main()
