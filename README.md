# dotDict
A simple Python library that builds upon `argparse.Namespace` to make chained attributes possible.

## Installation
Installation is simple: From this directory, run `pip install .`

## Usage
Usage is equally as simple:
```python
from dotdict import dotDict as dd

x = dd()

x.a.b.c = 1
x.a.d = 2
x.a.b.e = 3

print(x) # dotDict(a=dotDict(b=dotDict(c=1, e=3), d=2))
print(vars(x)) # {'a': dotDict(b=dotDict(c=1, e=3), d=2)}
print(vars(x.a)) # {'b': dotDict(c=1, e=3), 'd': 2}
```
