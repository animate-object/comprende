from comprende.core.comprende import Module, Question
from typing import List
from textblob import TextBlob, WordList


def important_words_analyzer(
    text: str,
    desired_ct: int = 1
) -> List[Question]:
    return []


def find_noun_phrases(
    text: str,
) -> WordList:
    blob = TextBlob(text)
    return blob.noun_phrases


IMPORTANT_WORDS = Module(
    analyze=important_words_analyzer
)
