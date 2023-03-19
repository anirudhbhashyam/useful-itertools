import itertools

from typing import Any
from typing import Generator
from typing import Iterable
from typing import Iterator


def take_tuples(g: Iterable[Any], *, n: int = 3) -> Iterator[tuple[Any, ...]]:
    """
    Progress an iterable in steps of `n`.
    """
    it = iter(g)
    return zip(*(itertools.islice(g, i, None, n) for i, g in enumerate(itertools.tee(it, n))))


def main() -> int:
    l = [1, 2, 3, 4, 5, 6, 7]
    for i in take_tuples(l, n = 3):
        print(i)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
