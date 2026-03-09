#!/usr/bin/env python3

players = {
    "alice": {
        "score": 2300,
        "active": True,
        "region": "north",
        "achievements": ["first_kill", "level_10", "boss_slayer",
                         "sharp_shooter", "collector"]
    },
    "bob": {
        "score": 1800,
        "active": True,
        "region": "east",
        "achievements": ["first_kill", "level_5", "collector"]
    },
    "charlie": {
        "score": 2150,
        "active": True,
        "region": "central",
        "achievements": ["first_kill", "level_10", "boss_slayer",
                         "arena_winner", "collector", "explorer", "veteran"]
    },
    "diana": {
        "score": 2050,
        "active": False,
        "region": "north",
        "achievements": ["first_kill", "level_10",
                         "explorer", "treasure_hunter"]
    }
}


def main() -> None:
    """Run the Game Analytics Dashboard.

    Demonstrates list, dict, and set comprehensions to analyze
    player data: scores, activity status, achievements, regions,
    and overall statistics.

    Prints:
        - High scorers, doubled scores, active players
        - Player scores, score categories, achievement counts
        - Unique players, achievements, and regions
        - Combined summary: average score and top performer
    """

    print("=== Game Analytics Dashboard ===\n")

    if len(players) == 0:
        print("No players to work with. Add players.\n")
        return

    print("=== List Comprehension Examples ===")
    high_scores = [k for k, v in players.items() if v['score'] > 2000]
    scores_doubled = [v['score'] * 2 for v in players.values()]
    active_names = [k for k, v in players.items() if v['active']]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_names}")
    print()

    print("=== Dict Comprehension Examples ===")
    active = {n: v for n, v in players.items() if v['active']}
    scores = {n: v['score'] for n, v in active.items()}
    categories = {
        'high': len([n for n, v in active.items() if v['score'] >= 2100]),
        'medium': len(
            [n for n, v in active.items() if 2000 <= v['score'] < 2100]
        ),
        'low': len([n for n, v in active.items() if v['score'] < 2000]),
    }
    achievements = {n: len(v['achievements']) for n, v in active.items()}
    print(f"Player scores: {scores}")
    print(f"Score categories: {categories}")
    print(f"Achievement counts: {achievements}")
    print()

    print("=== Set Comprehension Examples ===")
    player_set = {n for n in players}
    achiev_types = {
        ach
        for v in players.values()
        for ach in v['achievements']
    }
    regions = {v['region'] for v in players.values()}
    print(f"Unique players: {player_set}")
    print(f"Unique achievements: {achiev_types}")
    print(f"Active regions: {regions}")
    print()

    print("=== Combined Analysis ===")
    score_avg = sum(v['score'] for v in players.values()) / len(players)
    top = max(players, key=lambda name: players[name]['score'])
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(achiev_types)}")
    print(f"Average score: {score_avg}")
    print(f"Top performer: {top} ({players[top]['score']} points, " +
          f"{len(players[top]['achievements'])} achievements)")


if __name__ == "__main__":
    main()
