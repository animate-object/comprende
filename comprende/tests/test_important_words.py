import pytest
from comprende.util import full_text
from comprende.core.important_words import IMPORTANT_WORDS, find_noun_phrases, most_frequent_noun_phrases
from pprint import pprint


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


def test_most_frequent_noun_phrases(
    wn_face_coverings,
):
    all_by_frequency = most_frequent_noun_phrases(wn_face_coverings)
    five_most_frequent = most_frequent_noun_phrases(wn_face_coverings, 5)

    assert len(five_most_frequent) == 5
    assert len(all_by_frequency) > len(five_most_frequent)

    print(five_most_frequent)
