
"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {
        "preferred_genres": ["pop"],
        "preferred_moods": ["happy"],
        "target_energy": 0.8,
        "target_tempo_bpm": 120,
        "target_valence": 0.8,
        "target_danceability": 0.8,
        "target_acousticness": 0.2
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations")
    print("=" * 50)

    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"\n{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        if explanation and explanation != "general match":
            reasons = explanation.split(", ")
            print("   Reasons:")
            for reason in reasons:
                print(f"     - {reason}")
        else:
            print("   Reasons: General match")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()