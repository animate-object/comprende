from comprende.core.comprende import Module, Question
from typing import List, Optional, Dict
from textblob import TextBlob, WordList


def important_words_analyzer(
    text: str,
    desired_ct: int = 1
) -> List[Question]:
    return []


def most_frequent_noun_phrases(
    text: str,
    desired_ct: Optional[int] = None,
) -> Dict[str, int]:
    """Return a dict of up to {desired_ct} pairs
    of <noun_phrase>: <freq>

    Args:
        text (str): source text
        desired_ct (int): desired length of dictionary,
            None means include all noun phrases
            Can return less than desired_ct if there
            are not enough unique phrases

    Returns:
        Dict[str, int]: a mappping of noun phrases to frequency
    """
    blob = TextBlob(text)
    phrase_freq = (
        (phrase, blob.noun_phrases.count(phrase))
        for phrase in
        set(blob.noun_phrases)
    )
    if not desired_ct:
        return dict(phrase_freq)
    else:
        sorted_by_freq = sorted(
            phrase_freq,
            key=lambda t: t[1],
            reverse=True
        )
        print(sorted_by_freq)
        return dict(
            sorted_by_freq[:min(len(sorted_by_freq) - 1, desired_ct)]
        )


def find_noun_phrases(
    text: str,
) -> WordList:
    blob = TextBlob(text)
    return blob.noun_phrases


IMPORTANT_WORDS = Module(
    analyze=important_words_analyzer
)
