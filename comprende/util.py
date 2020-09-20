import os
from comprende.core.comprende import Module

SRC_DIR = os.path.dirname(__file__)
PROJ_ROOT = os.path.abspath(os.path.dirname(SRC_DIR))
TEST_DIR = os.path.join(SRC_DIR, 'tests')
DATA_DIR = os.path.join(TEST_DIR, 'data')

assert TEST_DIR.endswith('/comprende/tests')
assert PROJ_ROOT.endswith('/comprende')
assert DATA_DIR.endswith('/comprende/tests/data')


def full_text(
    file_path: str,
    root_dir: str = DATA_DIR,
) -> str:
    """Easily load test data by name

    Args:
        path (str): path to the file relative to {root_dir}
        root_dir (str, optional): directory to pull the file from. Defaults to DATA_DIR.

    Returns:
        str: the content of the file
    """
    path = os.path.join(root_dir, file_path)

    with open(path, 'r') as text_in:
        return text_in.read()


def perform_analysis(
    text: str,
    module: Module,
):
    result = module.analyze(text)
    return result
