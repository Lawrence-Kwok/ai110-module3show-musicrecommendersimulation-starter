"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


user_profiles = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.9,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "calm",
        "target_energy": 0.2,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.85,
        "likes_acoustic": False,
    },
}


def print_recommendations(profile_name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(f"\nTop recommendations for '{profile_name}':\n")
    print("=" * 60)

    for index, rec in enumerate(recommendations, start=1):
        song, score, reasons = rec

        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score   : {score:.2f}")
        print(f"   Genre   : {song['genre']}")
        print(f"   Mood    : {song['mood']}")
        print("   Reasons :")

        for reason in reasons:
            print(f"   - {reason}")

        print("-" * 60)


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in user_profiles.items():
        print_recommendations(profile_name, user_prefs, songs, k=5)


if __name__ == "__main__":
    main()
