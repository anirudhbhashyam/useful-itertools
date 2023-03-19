from itertools import chain, repeat

from typing import Iterable
from typing import TypeVar

T = TypeVar("T")


def first(g: Iterable[T], *, n: int = 1) -> zip[tuple[bool, T]]:
    return zip(chain(repeat(True, n), repeat(False)), g)


def main() -> int:
    print(list(first(range(1, 10))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
