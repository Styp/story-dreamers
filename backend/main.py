#!/usr/bin/env python
from fetch_images import fetch_image

test_str = "There was a miller whose only inheritance to his three sons was his mill, his donkey, and his cat. The division was soon made. They hired neither a clerk nor an attorney, for they would have eaten up all the poor patrimony. The eldest took the mill, the second the donkey, and the youngest nothing but the cat."

def sentence_tokenizer(text: str) -> str:
    for sentence_token in text.split("."):
        yield sentence_token


def main():
    for sentence_index, sentence in enumerate(sentence_tokenizer(test_str)):
        images = fetch_image(sentence)
        for index, image in enumerate(images):
            image.save(f'images/{sentence_index:03d}-{index:03d}.png')



if __name__ == "__main__":
    main()
