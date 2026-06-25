"""Code Nexus - Exercise 1: Polymorphic Processing of a Data Stream.

Builds on Exercise 0. A ``DataStream`` receives a heterogeneous list of
elements and, through polymorphism, routes each element to the first
registered processor that can validate it.
"""

from abc import ABC, abstractmethod
from typing import Any


class InvalidDataError(Exception):
    """Raised when a processor is asked to ingest data it cannot handle."""


class DataProcessor(ABC):
    """Abstract base for every data processor in the Code Nexus."""

    name: str = "Data Processor"

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True if ``data`` can be ingested by this processor."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process ``data`` and store it internally as string(s)."""

    def _store(self, value: str) -> None:
        self._storage.append((self._total, value))
        self._total += 1

    def output(self) -> tuple[int, str]:
        """Remove and return the oldest stored (rank, value) pair."""
        if not self._storage:
            raise InvalidDataError(f"{self.name}: nothing to output")
        return self._storage.pop(0)

    @property
    def total_processed(self) -> int:
        return self._total

    @property
    def remaining(self) -> int:
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


class DataStream:
    """Routes a heterogeneous stream to its registered processors."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    @property
    def processors(self) -> list[DataProcessor]:
        """The registered processors, in registration order."""
        return self._processors

    def register_processor(self, proc: DataProcessor) -> None:
        """Add a processor to the routing table (order matters)."""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Send each element to the first processor that accepts it."""
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print("DataStream error - Can't process element "
                      f"in stream: {element}")

    def print_processors_stats(self) -> None:
        """Print per-processor totals and remaining counts."""
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(f"{proc.name}: total {proc.total_processed} items "
                  f"processed, remaining {proc.remaining} on processor")


def main() -> None:
    """Demonstrate polymorphic routing and live statistics."""
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(NumericProcessor())

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    consume_plan = [("Numeric Processor", 3), ("Text Processor", 2),
                    ("Log Processor", 1)]
    by_name = {p.name: p for p in stream.processors}
    for name, count in consume_plan:
        for _ in range(count):
            by_name[name].output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
