import itertools

from typing import Generator
from typing import TypeVar
from typing import Iterable
from typing import Iterator

T = TypeVar("T")


def interleave(*iters: Iterable[T]) -> Iterator[T]:
    for z in itertools.chain.from_iterable(itertools.zip_longest(*iters)):
        if z is not None:
            yield z

def main() -> int:
    l1 = ["b", None, "m", None, "yzh"]
    l2 = ["a", "c",]
    for x in interleave(l2, l1):
        print(x)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
