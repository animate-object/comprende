import attr
from typing import Optional, List, Callable, Union, Generator


@attr.s(auto_attribs=True)
class Question:
    prompt: str
    correct_options: List[str]
    addition_option: List[str]


Analyzer = Callable[[str, int], List[Question]]


@attr.s(auto_attribs=True)
class Module():
    analyze: Analyzer
