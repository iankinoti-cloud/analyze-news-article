"""Text analysis functions for extracting insights from news articles."""

import re


def count_specific_word(text, word):
    """Return how many times `word` appears in `text` (case-insensitive)."""
    words = re.findall(r"[A-Za-z']+", text.lower())
    target = word.lower()
    count = 0
    index = 0
    while index < len(words):
        if words[index] == target:
            count += 1
        index += 1
    return count


def identify_most_common_word(text):
    """Return the most frequently occurring word in `text`."""
    words = re.findall(r"[A-Za-z']+", text.lower())
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    most_common_word = None
    highest_count = 0
    for word, count in frequency.items():
        if count > highest_count:
            most_common_word = word
            highest_count = count
    return most_common_word


def calculate_average_word_length(text):
    """Return the average length of the words in `text` as a float."""
    words = re.findall(r"[A-Za-z']+", text)
    if not words:
        return 0.0

    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length / len(words)


def count_paragraphs(text):
    """Return the number of paragraphs in `text`, separated by blank lines."""
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    """Return the number of sentences in `text`."""
    fragments = re.split(r"[.!?]+", text)
    count = 0
    for fragment in fragments:
        if fragment.strip():
            count += 1
    return count
