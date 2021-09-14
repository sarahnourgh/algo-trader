from typing import List, Iterator

from entities.candle import Candle
from pipeline.source import Source


class FakeSource(Source):
    def __init__(self, candles: List[Candle]) -> None:
        super().__init__()
        self.candles = candles

    def read(self) -> Iterator[Candle]:
        for c in self.candles:
            yield c