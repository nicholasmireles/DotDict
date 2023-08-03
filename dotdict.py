from typing import Any
from argparse import Namespace


class DotDict(Namespace):
    """A simple class that builds upon `argparse.Namespace`
    in order to make chained attributes possible."""

    def __init__(self, temp=False, key=None, parent=None) -> None:
        self._temp = temp
        self._key = key
        self._parent = parent

    def __eq__(self, other):
        if not isinstance(other, DotDict):
            return NotImplemented
        return vars(self) == vars(other)

    def __getattr__(self, __name: str) -> Any:
        if __name not in self.__dict__ and not self.temp:
            self.__dict__[__name] = DotDict(temp=True, key=__name, parent=self)
        else:
            del self.parent.__dict__[self.key]
            raise AttributeError("No attribute '%s'" % __name)
        return self.__dict__[__name]

    def __repr__(self) -> str:
        num_items = len([k for k in self.__dict__ if not k.startswith("_")])

        if num_items == 0:
            return "DotDict()"
        elif num_items == 1:
            key, val = self.__dict__.items()[0]
            return "DotDict(%s=%s)" % (key, repr(val))
        else:
            return "DotDict(%s)" % ", ".join(
                "%s=%s" % (key, repr(val)) for key, val in self.__dict__.items()
            )
