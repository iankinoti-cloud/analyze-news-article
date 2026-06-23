"""Demo script: run text analysis on the sample news article."""

from pythonAssessment import (
    count_specific_word,
    identify_most_common_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences,
)


def main():
    with open("article.txt", "r", encoding="utf-8") as f:
        article = f.read()

    search_word = "pie"

    print(f"'{search_word}' count: {count_specific_word(article, search_word)}")
    print(f"Most common word: {identify_most_common_word(article)}")
    print(f"Average word length: {calculate_average_word_length(article):.2f}")
    print(f"Paragraph count: {count_paragraphs(article)}")
    print(f"Sentence count: {count_sentences(article)}")


if __name__ == "__main__":
    main()
