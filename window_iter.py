import itertools

import pytest

from typing import Iterable
from typing import Iterator
from typing import TypeVar

T = TypeVar("T")


def window_iter(g: Iterable[T], *, n: int = 3) -> Iterator[tuple[T, ...]]:
    """
    Progress an iterable in window sizes of n.
    """
    it = iter(g)
    return zip(*(itertools.islice(g, i, None) for i, g in enumerate(itertools.tee(it, n))))


