from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.0

            score += max(0.0, 1.5 - abs(song.energy - user.target_energy) * 3)

            if user.likes_acoustic:
                score += max(0.0, 0.5 - abs(song.acousticness - 1.0))
            else:
                score += max(0.0, 0.5 - abs(song.acousticness - 0.0))

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("it matches your favorite genre")

        if song.mood == user.favorite_mood:
            reasons.append("it matches your favorite mood")

        if abs(song.energy - user.target_energy) < 0.15:
            reasons.append("its energy level is close to your preference")

        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append("it has a more acoustic sound")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("it has a less acoustic sound")

        if reasons:
            return f"Recommended because {', '.join(reasons)}."
        return "Recommended because it is a reasonably good overall match."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Scores a single song against user preferences.
    Expected user_prefs format:
    {"preferred_genres": ["pop"], "preferred_moods": ["happy"], "target_energy": 0.8, ...}
    Returns: (score, explanation)
    """
    score = 0.0
    reasons = []

    # Normalize tempo
    norm_tempo_song = (song["tempo_bpm"] - 60) / 92
    norm_tempo_target = (user_prefs["target_tempo_bpm"] - 60) / 92

    # Genre match
    if song["genre"] in user_prefs["preferred_genres"]:
        score += 30
        reasons.append("genre match")

    # Mood match
    if song["mood"] in user_prefs["preferred_moods"]:
        score += 20
        reasons.append("mood match")

    # Numeric features
    numerics = {
        "energy": (song["energy"], user_prefs["target_energy"]),
        "norm_tempo": (norm_tempo_song, norm_tempo_target),
        "valence": (song["valence"], user_prefs["target_valence"]),
        "danceability": (song["danceability"], user_prefs["target_danceability"]),
        "acousticness": (song["acousticness"], user_prefs["target_acousticness"])
    }

    for feature, (song_val, target_val) in numerics.items():
        closeness = 1 - abs(song_val - target_val)
        points = 10 * closeness
        score += points
        if closeness > 0.8:
            reasons.append(f"{feature} is close to your preference")

    explanation = ", ".join(reasons) if reasons else "general match"
    return score, explanation


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Returns: (song_dict, score, explanation)
    """
    scored_songs = [(song, *score_song(user_prefs, song)) for song in songs]
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]