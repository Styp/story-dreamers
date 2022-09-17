#!/usr/bin/env python
import os
import shutil
from os import path
from typing import Dict

from backend.services.prompt_extractor import PromptExtractor
from fetch_images import fetch_image

test_str = "There was a miller whose only inheritance to his three sons was his mill, his donkey, and his cat. The division was soon made. They hired neither a clerk nor an attorney, for they would have eaten up all the poor patrimony. The eldest took the mill, the second the donkey, and the youngest nothing but the cat. + oil painting"


def sentence_tokenizer(text: str) -> str:
    for sentence_token in text.split("."):
        yield sentence_token


def file_tokenizer(file_to_test: str, prompt_extractor: PromptExtractor) -> Dict[str, str]:
    with open((path.join("test-books", file_to_test))) as story_file:
        return prompt_extractor.extract_paragraphs_with_prompts(story_file.read())


def recreate_image_directory():
    file_path = os.path.dirname(os.path.realpath(__file__))
    image_directory = os.path.join(file_path, 'images')
    shutil.rmtree(image_directory)
    os.mkdir(image_directory)
    return image_directory


def main():
    prompt_extractor = PromptExtractor()
    file_to_test = "snowwhite.txt"
    image_directory = recreate_image_directory()
    for sentence_index, sentence in enumerate(file_tokenizer(file_to_test, prompt_extractor).values()):
        try:
            print("sentence: ", sentence)
            images = fetch_image(sentence)
            for index, image in enumerate(images):
                image.save(os.path.join(image_directory, f'{sentence_index:03d}-{index:03d}.png'))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
