#!/usr/bin/env python
from os import path
from rake_nltk import Rake
import nltk
from fetch_images import fetch_image

test_str = "There was a miller whose only inheritance to his three sons was his mill, his donkey, and his cat. The division was soon made. They hired neither a clerk nor an attorney, for they would have eaten up all the poor patrimony. The eldest took the mill, the second the donkey, and the youngest nothing but the cat."


def get_summary(text: str) -> str:
    print("input: ", text)
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()[0]
    print(keyword_extracted)
    return keyword_extracted + " oil painting"


def sentence_tokenizer(text: str) -> str:
    for sentence_token in text.split("."):
        yield sentence_token


def file_tokenizer(file_to_test: str) -> str:
    with open((path.join("test-books", file_to_test))) as story_file:

        paragraph = ""
        line_with_content_counter = 0
        for idx, line in enumerate(story_file):
            if line.strip():
                line_with_content_counter += 1
                paragraph += line
            if line_with_content_counter == 3:
                line_with_content_counter = 0
                input = paragraph
                paragraph = ""
                yield get_summary(input)


def main():
    nltk.download('punkt')
    nltk.download('stopwords')
    file_to_test = "snowwhite.txt"
    for sentence_index, sentence in enumerate(file_tokenizer(file_to_test)):
        try:
            images = fetch_image(sentence)
            for index, image in enumerate(images):
                image.save(f'images/{sentence_index:03d}-{index:03d}.png')
        except Exception as e:
            print(e)



if __name__ == "__main__":
    main()
