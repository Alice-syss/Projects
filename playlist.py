import random

songs = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop"},
    {"title": "HUMBLE.", "artist": "Kendrick Lamar", "genre": "Hip-Hop"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock"},
    {"title": "Bad Guy", "artist": "Billie Eilish", "genre": "Pop"},
    {"title": "God's Plan", "artist": "Drake", "genre": "Hip-Hop"},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "Rock"},
    {"title": "As It Was", "artist": "Harry Styles", "genre": "Pop"},
    {"title": "SICKO MODE", "artist": "Travis Scott", "genre": "Hip-Hop"},
    {"title": "Levitating", "artist": "Dua Lipa", "genre": "Pop"},
    {"title": "Lose Yourself", "artist": "Eminem", "genre": "Hip-Hop"},
]


def generate_playlist():
    print("🎵 Welcome to the Random Playlist Generator!")

    amount = input("\nHow many songs do you want in your playlist? ")

    if not amount.isdigit():
        print("Please enter a valid number!")
        return generate_playlist()

    amount = int(amount)

    if amount > len(songs):
        print(f"I only have {len(songs)} songs available! Generating full playlist.")
        amount = len(songs)

    playlist = random.sample(songs, amount)

    print(f"\n🎧 Your Playlist ({amount} songs):")
    print("-" * 40)

    for i, song in enumerate(playlist, 1):
        print(f"{i}. {song['title']} - {song['artist']} [{song['genre']}]")

    print("-" * 40)

    again = input("\nGenerate another playlist? (yes/no): ")
    if again.lower() == "yes":
        generate_playlist()


generate_playlist()

