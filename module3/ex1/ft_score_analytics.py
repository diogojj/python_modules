import sys


def main() -> None:
    """Read scores from argv, drop invalid ones, print basic statistics."""
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for raw in sys.argv[1:]:
        try:
            scores.append(int(raw))
        except ValueError:
            print(f"Invalid parameter: '{raw}'")
    if len(scores) == 0:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return
    total: int = sum(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
