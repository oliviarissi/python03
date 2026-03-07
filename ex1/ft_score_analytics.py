#!/usr/bin/env python3

import sys


def calculate_stats(scores: list) -> None:
    if not scores:
        print("There are no valid scores to analyze")
        return

    print(f"Total players: {len(scores)}\n" +
          f"Total score: {sum(scores)}\n" +
          f"Average score: {sum(scores)/len(scores)}\n" +
          f"High score: {max(scores)}\n" +
          f"Low score: {min(scores)}\n" +
          f"Score range: {max(scores) - min(scores)}\n")


def main() -> None:

    print("=== Player Score Analytics ===\n")

    argc = len(sys.argv)
    scores = []

    if argc == 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} " +
              "<score1> <score2> ...")
        return

    for item in sys.argv[1:]:
        try:
            score = int(item)
            scores.append(score)
        except ValueError:
            print(f"! Ignoring invalid score: '{item}'")

    print(f"Scores processed: {scores}\n")

    calculate_stats(scores)


if __name__ == "__main__":
    main()
