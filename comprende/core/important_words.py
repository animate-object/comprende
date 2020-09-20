from comprende.core.comprende import Module, Question
from typing import List, Optional, Tuple, Dict, Union
from textblob import TextBlob, WordList
from enum import Enum
from random import choice, seed, shuffle
from math import floor
from collections import defaultdict

seed()


class ImportantWordQuestionType(Enum):
    MOST = (
        'Which of these key phrases was mentioned often in this document?',
        {
            'least_frequent': False,
        }
    )

    LEAST = (
        'Which of these key phrases was mentioned in this document?',
        {
            'least_frequent': True,
        }
    )

    ALL = (
        'Which of these phrases was mentioned in this document?',
        {
            'least_frequent': True,
            'request_all': True,
        }
    )

    @property
    def prompt(self) -> str:
        return self.value[0]

    @property
    def config_opts(self) -> Dict:
        return defaultdict(lambda: None, self.value[1])


ALL_Q_TYPES = [
    ImportantWordQuestionType.MOST,
    ImportantWordQuestionType.LEAST,
]


def important_words_analyzer(
    text: Union[str, TextBlob],
    desired_ct: int = 1,
    strip_first_sentence: bool = True,
    allow_q_types: List[ImportantWordQuestionType] = ALL_Q_TYPES,
    fuzz_by: float = 0,
) -> List[Question]:
    blob = text if type(text) == TextBlob else TextBlob(text)
    if strip_first_sentence and len(blob.sentences) > 1:
        blob = TextBlob(blob.raw[blob.sentences[0].end:])

    q_type = choice(allow_q_types)
    q_config = q_type.config_opts

    noun_phrase_ct = None
    if not q_config['request_all']:
        extra_ = floor(fuzz_by * len(blob.noun_phrases))
        noun_phrase_ct = min(desired_ct + extra_, len(blob.noun_phrases))

    phrases = frequent_noun_phrases(
        blob, noun_phrase_ct, q_config['least_frequent']
    )

    if fuzz_by:
        shuffle(phrases)

    return [
        Question(prompt=q_type.prompt, correct_options=[p])
        for p in
        phrases
    ]


def frequent_noun_phrases(
    text: TextBlob,
    desired_ct: Optional[int] = None,
    least_frequent: bool = False,
) -> Tuple[str, int]:
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
    phrase_freq = (
        (phrase, text.noun_phrases.count(phrase))
        for phrase in
        set(text.noun_phrases)
    )
    if not desired_ct:
        return phrase_freq
    else:
        sorted_by_freq = sorted(
            phrase_freq,
            key=lambda t: t[1],
            reverse=not least_frequent,
        )
        return sorted_by_freq[:min(len(sorted_by_freq) - 1, desired_ct)]


IMPORTANT_WORDS = Module(
    analyze=important_words_analyzer
)
