"""Code Nexus - Exercise 2: Data Pipeline.

Builds on Exercise 1. The output side of the pipeline is a plugin
system: any object that structurally matches the ``ExportPlugin``
protocol (duck typing) can receive consumed data. Two plugins are
provided: CSV and JSON, both building their strings by hand.
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    """Structural contract every export plugin must satisfy.

    Inheriting from ``Protocol`` means compatibility is checked by shape
    (duck typing), not by inheritance: any class that defines a matching
    ``process_output`` is accepted, even without subclassing this.
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Export a batch of consumed (rank, value) pairs."""
        ...


class CSVExportPlugin:
    """Exports values as a single comma-separated line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        line = ",".join(value for _, value in data)
        print("CSV Output:")
        print(line)


class JSONExportPlugin:
    """Exports values as a JSON object keyed by 'item_<rank>'."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print("JSON Output:")
        print("{" + pairs + "}")


class DataStream:
    """Routes input streams and pipes consumed output to plugins."""

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume up to ``nb`` items per processor; export each batch."""
        for proc in self._processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining == 0:
                    break
                batch.append(proc.output())
            plugin.process_output(batch)


def main() -> None:
    """Demonstrate the full input -> route -> export pipeline."""
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1: list[Any] = [
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
    print(f"\nSend first batch of data on stream: {batch1}\n")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()

    batch2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch2}\n")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
