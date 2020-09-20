import attr
from typing import Optional, List, Callable, Union, Generator
from textblob import TextBlob


@attr.s(auto_attribs=True)
class Question:
    prompt: str
    correct_options: List[str]
    module_name: str
    additional_option: List[str] = []
    subtype: Optional[str] = None


Analyzer = Callable[[TextBlob, int], List[Question]]


@attr.s(auto_attribs=True)
class Module():
    analyze: Analyzer
