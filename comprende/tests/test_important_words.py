import pytest
from comprende.util import full_text
from comprende.core.important_words import IMPORTANT_WORDS, find_noun_phrases, frequent_noun_phrases
from pprint import pprint
from statistics import mean


@pytest.fixture
def wn_face_coverings():
    text = full_text('wikinews/face_coverings_to_be_mandatory')
    assert len(text) > 0
    return text


def test_important_words__produces_result():
    print(wn_face_coverings)

    questions = IMPORTANT_WORDS.analyze("")

    assert questions is not None
    assert type(questions) is list


def test_important_words__produces_questions(
    wn_face_coverings,
):
    pass


def test_noun_phrases(
    wn_face_coverings,
):
    noun_phrases = find_noun_phrases(wn_face_coverings)
    pprint([n for n in noun_phrases])


def test_frequent_noun_phrases(
    wn_face_coverings,
):
    all_by_frequency = frequent_noun_phrases(wn_face_coverings)
    four_most_frequent = frequent_noun_phrases(wn_face_coverings, 4)
    four_least_frequent = frequent_noun_phrases(wn_face_coverings, 4, True)

    assert len(all_by_frequency) > 4
    assert len(four_most_frequent) == 4
    assert all(v > 1 for v in four_most_frequent.values())
    assert len(all_by_frequency) > len(four_most_frequent)
    assert mean(four_most_frequent.values()) > mean(all_by_frequency.values())
    assert mean(all_by_frequency.values()) > mean(four_least_frequent.values())
