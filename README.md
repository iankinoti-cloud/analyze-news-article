# Analyze News Article

A lean Python toolkit that rips a news article apart and hands you the numbers that matter — word frequency, sentence rhythm, paragraph structure, and more. Built for text analysis pipelines that need fast, dependency-free insights.

## What it does

| Function | Returns |
|---|---|
| `count_specific_word(text, word)` | How many times a word shows up (case-insensitive) |
| `identify_most_common_word(text)` | The single most frequent word in the text |
| `calculate_average_word_length(text)` | Average word length, as a float |
| `count_paragraphs(text)` | Number of paragraphs (blank-line separated) |
| `count_sentences(text)` | Number of sentences |

No external dependencies — just the Python standard library (`re`).

## Quick start

```bash
git clone https://github.com/iankinoti-cloud/analyze-news-article.git
cd analyze-news-article
python3 main.py
```

`main.py` runs every function against `article.txt` (a sample ACME Inc. press release) and prints the results:

```
'pie' count: 21
Most common word: the
Average word length: 5.27
Paragraph count: 19
Sentence count: 48
```

## Using it on your own text

```python
from pythonAssessment import (
    count_specific_word,
    identify_most_common_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences,
)

with open("your_article.txt") as f:
    text = f.read()

print(count_specific_word(text, "innovation"))
print(identify_most_common_word(text))
print(calculate_average_word_length(text))
print(count_paragraphs(text))
print(count_sentences(text))
```

## Project structure

```
.
├── article.txt          # sample news article
├── main.py              # demo runner
├── pythonAssessment.py  # core analysis functions
└── README.md
```

## License

MIT
