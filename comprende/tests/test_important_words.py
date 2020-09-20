import pytest
from comprende.util import full_text
from comprende.core.important_words import (
    frequent_noun_phrases,
    ImportantWordQuestionType,
    important_words_analyzer,
)
from pprint import pprint
from statistics import mean
from textblob import TextBlob


@pytest.fixture
def wn_face_coverings():
    text = full_text('wikinews/face_coverings')
    assert len(text) > 0
    return text


def test_q_types():
    assert ImportantWordQuestionType.MOST.config_opts['asdf'] == None


def test_important_words__produces_result():
    questions = important_words_analyzer("")

    assert questions is not None
    assert type(questions) is list


def test_important_words__produces_questions(
    wn_face_coverings,
):
    qs = important_words_analyzer(
        wn_face_coverings,
        desired_ct=1,
        allow_q_types=[ImportantWordQuestionType.MOST]
    )
    assert len(qs) == 1


def test_with_fuzzing(
    wn_face_coverings,
):
    qs = [important_words_analyzer(
        TextBlob(wn_face_coverings),
        desired_ct=1,
        allow_q_types=[ImportantWordQuestionType.MOST],
        fuzz_by=.1
    ) for i in range(30)]

    unique_answers = set(q[0].correct_options[0] for q in qs)
    assert len(unique_answers) > 1


def test_frequent_noun_phrases(
    wn_face_coverings,
):
    blob = TextBlob(wn_face_coverings)
    all_by_frequency = dict(frequent_noun_phrases(blob))
    four_most_frequent = dict(frequent_noun_phrases(blob, 4))
    four_least_frequent = dict(frequent_noun_phrases(blob, 4, True))

    assert len(all_by_frequency) > 4
    assert len(four_most_frequent) == 4
    assert all(v > 1 for v in four_most_frequent.values())
    assert len(all_by_frequency) > len(four_most_frequent)
    assert mean(four_most_frequent.values()) > mean(all_by_frequency.values())
    assert mean(all_by_frequency.values()) > mean(four_least_frequent.values())
