import itertools

from typing import TypeVar
from typing import Iterable
from typing import Iterator
from typing import NoReturn


T = TypeVar("T")


def interleave(*iters: Iterable[T]) -> Iterator[T]:
    """
    Interleave iterables.
    """
    for z in itertools.chain.from_iterable(itertools.zip_longest(*iters)):
        if z is not None:
            yield z
