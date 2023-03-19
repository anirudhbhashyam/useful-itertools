from itertools import chain, repeat

from typing import Iterable
from typing import Iterator
from typing import TypeVar
from typing import NoReturn

import pytest


T = TypeVar("T")


def first(g: Iterable[T], *, n: int = 1) -> Iterator[tuple[bool, T]]:
    """
    Returns boolean values attached to the original iterable 
    that indicates which element is the first.
    """
    return zip(chain(repeat(True, n), repeat(False)), iter(g))


@pytest.mark.parametrize(
    ("iterable"),
    [
        range(1, 3), 
        [(True, 1), (False, 2)],
        "ghe"
    ]
)
def test_first(iterable: Iterable[T]) -> NoReturn:
    assert next(first(iterable))[1] == next(iter(iterable))
