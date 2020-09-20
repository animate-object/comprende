import attr
from typing import Optional, List, Callable, Union, Generator, Dict, Any
from textblob import TextBlob
from attr import asdict
from json import dumps
from comprende.core.util import non_null

DebugInfo = Dict[str, Any]
Kwargs = Dict[str, Any]


@attr.s(auto_attribs=True)
class Question:
    prompt: str
    correct_options: List[str]
    module_name: str
    additional_option: List[str] = []
    subtype: Optional[str] = None
    debug: Optional[DebugInfo] = None

    def as_dict(self):
        return non_null(asdict(self))

    @staticmethod
    def as_json(*questions: List['Question']):
        return dumps(
            [q.as_dict() for q in questions]
        )


Analyzer = Callable[[
    TextBlob,
    int,
    Optional[Kwargs]
], List[Question]]


@ attr.s(auto_attribs=True)
class Module():
    analyze: Analyzer
