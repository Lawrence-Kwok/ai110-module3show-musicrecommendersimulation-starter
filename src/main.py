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

    user_prefs = {
        "favorite_genre": "pop", 
        "favorite_mood": "happy", 
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
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


if __name__ == "__main__":
    main()
