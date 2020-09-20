import os
from comprende.core.types import Module, Question
from comprende.core.comprende import ALL_MODULES
from typing import List, Optional, Generator
from textblob import TextBlob
from random import choice, seed
from itertools import chain


SRC_DIR = os.path.dirname(__file__)
PROJ_ROOT = os.path.abspath(os.path.dirname(SRC_DIR))
TEST_DIR = os.path.join(SRC_DIR, 'tests')
DATA_DIR = os.path.join(TEST_DIR, 'data')

assert TEST_DIR.endswith('/comprende/tests')
assert PROJ_ROOT.endswith('/comprende')
assert DATA_DIR.endswith('/comprende/tests/data')


def full_text(
    file_path: str,
    root_dir: Optional[str] = DATA_DIR,
) -> str:
    """Easily load test data by name

    Args:
        path (str): path to the file relative to {root_dir}
        root_dir (str, optional): directory to pull the file from. Defaults to DATA_DIR.

    Returns:
        str: the content of the file
    """
    path = os.path.join(root_dir, file_path) \
        if root_dir else file_path

    with open(path, 'r') as text_in:
        return text_in.read()


def analyze_file(
    file_path: str,
    local_data: bool = True,
    modules: List[Module] = ALL_MODULES,
    desired_ct: int = 1
) -> Generator[Question, None, None]:

    text = full_text(
        file_path,
        root_dir=DATA_DIR if local_data else None,
    )
    blob = TextBlob(text)

    return chain(choice(modules).analyze(blob, 1)[0] for _ in range(desired_ct))
