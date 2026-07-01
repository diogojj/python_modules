"""Code Nexus - Exercise 0: Data Processor.

Foundation of the data-processing system: an abstract base class that
fixes a common interface (validate / ingest / output) and three
specialised processors that override the interface for their own data
types while sharing the same extraction mechanism.
"""

from abc import ABC, abstractmethod
from typing import Any


class InvalidDataError(Exception):
    """Raised when a processor is asked to ingest data it cannot handle."""


class DataProcessor(ABC):
    """Abstract base for every data processor in the Code Nexus.

    Every ingested item is stored together with a monotonically
    increasing *processing rank*, and items are extracted in FIFO order
    (oldest first) through ``output``.
    """

    name: str = "Data Processor"

    def __init__(self) -> None:
        # FIFO buffer of (rank, stringified value) pairs.
        self._storage: list[tuple[int, str]] = []
        # Total items ever ingested; also the next rank to assign.
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True if ``data`` can be ingested by this processor."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process ``data`` and store it internally as string(s)."""

    def _store(self, value: str) -> None:
        """Store one already-stringified value with its processing rank."""
        self._storage.append((self._total, value))
        self._total += 1

    def output(self) -> tuple[int, str]:
        """Remove and return the oldest stored (rank, value) pair."""
        if not self._storage:
            raise InvalidDataError(f"{self.name}: nothing to output")
        return self._storage.pop(0)

    @property
    def total_processed(self) -> int:
        """Total number of items ever ingested by this processor."""
        return self._total

    @property
    def remaining(self) -> int:
        """Number of items still waiting to be extracted."""
        return len(self._storage)


class NumericProcessor(DataProcessor):
    """Processes ints, floats and (possibly mixed) lists of them."""

    name = "Numeric Processor"

    @staticmethod
    def _is_number(value: Any) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return len(data) > 0 and all(self._is_number(x) for x in data)
        return self._is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise InvalidDataError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for value in items:
            self._store(str(value))


class TextProcessor(DataProcessor):
    """Processes strings and lists of strings."""

    name = "Text Processor"

    @staticmethod
    def _is_text(value: Any) -> bool:
        return isinstance(value, str)

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return len(data) > 0 and all(self._is_text(x) for x in data)
        return self._is_text(data)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise InvalidDataError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for value in items:
            self._store(value)


class LogProcessor(DataProcessor):
    """Processes log dicts ({str: str}) and lists of such dicts."""

    name = "Log Processor"

    @staticmethod
    def _is_log(value: Any) -> bool:
        if not isinstance(value, dict):
            return False
        if "log_level" not in value or "log_message" not in value:
            return False
        return all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in value.items()
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return len(data) > 0 and all(self._is_log(x) for x in data)
        return self._is_log(data)

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise InvalidDataError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for entry in items:
            line = f"{entry['log_level']}: {entry['log_message']}"
            self._store(line)


def main() -> None:
    """Demonstrate validation, guarded ingestion and extraction."""
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' "
          "without prior validation:")
    try:
        num.ingest("foo")  # invalid on purpose -> intended mypy warning
    except InvalidDataError as exc:
        print(f" Got exception: {exc}")
    numbers: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {numbers}")
    num.ingest(numbers)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f" Trying to validate input '42': {txt.validate(42)}")
    words: list[str] = ["Hello", "Nexus", "World"]
    print(f" Processing data: {words}")
    txt.ingest(words)
    print(" Extracting 1 value...")
    rank, value = txt.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    logs: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {logs}")
    log.ingest(logs)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
