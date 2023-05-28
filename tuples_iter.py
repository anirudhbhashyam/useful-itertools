import itertools

import pytest

from typing import Iterable
from typing import Iterator
from typing import TypeVar

T = TypeVar("T")


def take_tuples(g: Iterable[T], *, n: int = 3) -> Iterator[tuple[T, ...]]:
    """
    Progress an iterable in steps of `n`.
    """
    it = iter(g)
    return zip(*(itertools.islice(g, i, None, n) for i, g in enumerate(itertools.tee(it, n))))


@pytest.mark.parametrize(
    "input, n, expected_output", 
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [(1, 2, 3), (4, 5, 6)]),
        ([1, 2, 3, 4, 5, 6, 7], 2, [(1, 2), (3, 4), (5, 6)]),
        ("abfg", 2, [("a", "b"), ("f", "g")]),
        (("-1", "-2", "-3", "-10"), 2, [("-1", "-2"), ("-3", "-10")]),
        ((), 2, []),
    ]
)
def test_take_tuples(input: Iterable[T], n: int, expected_output: list[tuple[T, ...]]) -> None:
    assert list(take_tuples(input, n = n)) == expected_output


def main() -> int:
    l = (1, 2, 3)
    for i in take_tuples(l, n = 3):
        print(i)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
