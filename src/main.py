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

    profiles = {
        "High-Energy Pop": {
            "preferred_genres": ["pop"],
            "preferred_moods": ["happy"],
            "target_energy": 0.9,
            "target_tempo_bpm": 125,
            "target_valence": 0.85,
            "target_danceability": 0.85,
            "target_acousticness": 0.15
        },
        "Chill Lofi": {
            "preferred_genres": ["lofi", "ambient"],
            "preferred_moods": ["chill", "focused", "relaxed"],
            "target_energy": 0.35,
            "target_tempo_bpm": 75,
            "target_valence": 0.60,
            "target_danceability": 0.55,
            "target_acousticness": 0.80
        },
        "Deep Intense Rock": {
            "preferred_genres": ["rock"],
            "preferred_moods": ["intense", "moody"],
            "target_energy": 0.90,
            "target_tempo_bpm": 145,
            "target_valence": 0.45,
            "target_danceability": 0.60,
            "target_acousticness": 0.10
        },
        "Edge Case: High Energy but Sad": {
            "preferred_genres": ["pop", "rock"],
            "preferred_moods": ["sad", "melancholic"],
            "target_energy": 0.90,
            "target_tempo_bpm": 130,
            "target_valence": 0.20,
            "target_danceability": 0.70,
            "target_acousticness": 0.30
        }
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name}")
        print("=" * 60)

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

        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()