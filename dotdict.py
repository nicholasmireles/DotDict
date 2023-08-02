from typing import Any
from argparse import Namespace


class dotDict(Namespace):
    def __eq__(self, other):
        if not isinstance(other, dotDict):
            return NotImplemented
        return vars(self) == vars(other)

    def __contains__(self, key):
        return key in self.__dict__

    def __getattr__(self, __name: str) -> Any:
        if __name not in self.__dict__:
            self.__dict__[__name] = dotDict()
        return self.__dict__[__name]
