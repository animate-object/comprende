from typing import Dict


def non_null(d: Dict) -> Dict:
    return {
        i[0]: i[1]
        for i in d.items()
        if i[1] is not None
    }
