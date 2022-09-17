import unittest
from os import path

from backend.prompt_extractor import PromptExtractor


class MyTestCase(unittest.TestCase):

    def test_something(self):
        file_to_test = "snowwhite-test.txt"
        prompt_extractor = PromptExtractor()
        result = {}
        with open((path.join("test-data", file_to_test))) as story_file:
            result = prompt_extractor.extract_paragraphs_with_prompts(story_file.read())

        all_prompts = " ".join(str(x) for x in result.values())
        print(all_prompts)
        self.assertTrue("princess" in all_prompts)
        self.assertTrue("queen" in all_prompts)
        self.assertTrue("woods" in all_prompts)
        self.assertTrue("wolves" in all_prompts)
        self.assertTrue("cottage" in all_prompts)
        self.assertTrue("Dwarfs" in all_prompts)
        self.assertTrue("apple" in all_prompts)


if __name__ == '__main__':
    unittest.main()
