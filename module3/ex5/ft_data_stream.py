import random
import typing

PLAYERS: list[str] = ["nova", "echo", "rex", "sky", "zane"]
ACTIONS: list[str] = ["jump", "shoot", "dash", "block", "heal", "scan"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Endless generator yielding a random (player, action) event."""
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    """Pop a random event from the list and yield it until it is empty."""
    while len(events) > 0:
        index: int = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    """Stream 1000 events, build a list of 10, then consume it randomly."""
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
