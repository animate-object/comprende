import pytest
from comprende.util import full_text
from comprende.core.important_words import IMPORTANT_WORDS, find_noun_phrases
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
    find_noun_phrases(wn_face_coverings)
