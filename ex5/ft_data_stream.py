#!/usr/bin/env python3

from typing import Generator
import time

game_events = []


def event_stream(events: list[dict]) -> Generator[dict, None, None]:
    """Yield events one by one from a list.

    Args:
        events: List of game event dictionaries.

    Yields:
        dict: Next event from the list.
    """

    for event in events:
        yield event


def fibonacci(n: int) -> Generator[int, None, None]:
    """Generate the first n Fibonacci numbers.

    Args:
        n: Number of Fibonacci numbers to generate.

    Yields:
        int: Next number in the Fibonacci sequence.
    """

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(num: int) -> bool:
    """Check if a number is prime.

    Args:
        num: Integer to check.

    Returns:
        bool: True if num is prime, False otherwise.
    """

    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes(n: int) -> Generator[int, None, None]:
    """Generate the first n prime numbers.

    Args:
        n: Number of prime numbers to generate.

    Yields:
        int: Next prime number in sequence.
    """

    nb = 2
    reps = 0
    while reps < n:
        if is_prime(nb):
            yield nb
            reps += 1
        nb += 1


def main() -> None:
    """Process game events and print analytics.

    Uses a streaming generator to process events, counts high-level
    players, treasure events, and level-ups, and prints timing info.
    """

    stream = event_stream(game_events)

    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {len(game_events)} game events...\n")

    if len(game_events) == 0:
        print("No events to work with. Add events.\n")
        return

    total_events = 0
    top_players = 0
    treasures = 0
    level_ups = 0
    start_time = time.time()

    for event in stream:
        total_events += 1
        if event['data']['level'] > 10:
            top_players += 1
        if event['event_type'] == "item_found":
            treasures += 1
        if event['event_type'] == "level_up":
            level_ups += 1
        print(f"Event {event['id']}: Player {event['player']} " +
              f"(level {event['data']['level']}) {event['event_type']}")

    end_time = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {top_players}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_ups}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {(end_time - start_time):.2f} seconds\n")


def demonstrator() -> None:
    """Demonstrate generator usage.

    Prints the first 10 Fibonacci numbers and first 5 prime numbers.
    """

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): " +
          f"{", ".join(str(nb) for nb in fibonacci(10))}")
    print(f"Prime numbers (first 5): {", ".join(str(nb) for nb in primes(5))}")


if __name__ == "__main__":
    main()
    demonstrator()
