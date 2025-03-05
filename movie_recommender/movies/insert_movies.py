import os
import django

# Django-Umgebung laden
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")
django.setup()

from movies.models import Movie

movies = [
    # Action
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1, "poster_url": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg"},
    {"title": "John Wick", "genre": "Action", "rating": 7.4, "poster_url": "https://image.tmdb.org/t/p/w500/c9XxwwhPHdaImA2f1WEfEsbhaFB.jpg"},
    {"title": "Gladiator", "genre": "Action", "rating": 8.5, "poster_url": "https://image.tmdb.org/t/p/w500/o2jA9bGBLrJCC5K3B5E6Am7j5IT.jpg"},
    {"title": "Die Hard", "genre": "Action", "rating": 8.2, "poster_url": "https://image.tmdb.org/t/p/w500/yFihWxQcmqcaBR31QM6Y8gT6aYV.jpg"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4, "poster_url": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"},
    {"title": "Black Panther", "genre": "Action", "rating": 7.3, "poster_url": "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg"},
    {"title": "Thor: Ragnarok", "genre": "Action", "rating": 7.9, "poster_url": "https://image.tmdb.org/t/p/w500/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg"},
    {"title": "Logan", "genre": "Action", "rating": 8.1, "poster_url": "https://image.tmdb.org/t/p/w500/gGBu0hKw9BGddG8RkRAMX7B6NDB.jpg"},
    {"title": "Deadpool", "genre": "Action", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/fSRb7vyIP8rQpL0I47P3qUsEKX3.jpg"},
    {"title": "The Equalizer", "genre": "Action", "rating": 7.2, "poster_url": "https://image.tmdb.org/t/p/w500/2eQfjqlvPAxd9aLDs8DvsKLnfed.jpg"},
    {"title": "Atomic Blonde", "genre": "Action", "rating": 6.7, "poster_url": "https://image.tmdb.org/t/p/w500/kVZOE5MGSWXPZiD28jFy0f3h9SY.jpg"},
    {"title": "Mission: Impossible – Fallout", "genre": "Action", "rating": 7.8, "poster_url": "https://image.tmdb.org/t/p/w500/AkJQpZp9WoNdj7pLYSj1L0RcMMN.jpg"},
    {"title": "Pacific Rim", "genre": "Action", "rating": 6.9, "poster_url": "https://image.tmdb.org/t/p/w500/vVpEOvdxVBP2aV166j5Xlvb5Cdc.jpg"},
    {"title": "Fast & Furious 7", "genre": "Action", "rating": 7.1, "poster_url": "https://image.tmdb.org/t/p/w500/ktofZ9Htrjiy0P6LEowsDaxd3Ri.jpg"},

    # Sci-Fi
    {"title": "Blade Runner 2049", "genre": "Sci-Fi", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg"},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "poster_url": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "poster_url": "https://image.tmdb.org/t/p/w500/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg"},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "poster_url": "https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"},
    {"title": "The Martian", "genre": "Sci-Fi", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/5BHuvQ6p9kfc091Z8RiFNhCwL4b.jpg"},
    {"title": "Blade Runner 2049", "genre": "Sci-Fi", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg"},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "poster_url": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "poster_url": "https://image.tmdb.org/t/p/w500/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg"},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "poster_url": "https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"},
    {"title": "The Martian", "genre": "Sci-Fi", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/5BHuvQ6p9kfc091Z8RiFNhCwL4b.jpg"},
    {"title": "Avatar", "genre": "Sci-Fi", "rating": 7.8, "poster_url": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg"},
    {"title": "Guardians of the Galaxy", "genre": "Sci-Fi", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/r7vmZjiyZw9rpJMQJdXpjgiCOk9.jpg"},
    {"title": "Star Wars: A New Hope", "genre": "Sci-Fi", "rating": 8.6, "poster_url": "https://image.tmdb.org/t/p/w500/bDWF4FHVWl2hdhKpZQ88S8dNlWz.jpg"},
    {"title": "Dune", "genre": "Sci-Fi", "rating": 8.2, "poster_url": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg"},
    {"title": "Tenet", "genre": "Sci-Fi", "rating": 7.4, "poster_url": "https://image.tmdb.org/t/p/w500/k68nPLbIST6NP96JmTxmZijEvCA.jpg"},
    {"title": "Edge of Tomorrow", "genre": "Sci-Fi", "rating": 7.9, "poster_url": "https://image.tmdb.org/t/p/w500/uUH6k2X27LCYqbyZ2D71lfTy4el.jpg"},
    {"title": "Elysium", "genre": "Sci-Fi", "rating": 6.6, "poster_url": "https://image.tmdb.org/t/p/w500/qBD6jjIv9788UztVYpqvftJU6uN.jpg"},
    {"title": "The Fifth Element", "genre": "Sci-Fi", "rating": 7.7, "poster_url": "https://image.tmdb.org/t/p/w500/fPtlCO1yQtnoLHOwKtWz7db6RGU.jpg"},
    {"title": "Oblivion", "genre": "Sci-Fi", "rating": 7.0, "poster_url": "https://image.tmdb.org/t/p/w500/8NTaGPKr6cF9yrRhp8cXEWyAK9c.jpg"},
    {"title": "Arrival", "genre": "Sci-Fi", "rating": 7.9, "poster_url": "https://image.tmdb.org/t/p/w500/yNwKprjSC2xaygT3QFm0lQldpCy.jpg"},
    
    # Drama
    {"title": "Schindlers Liste", "genre": "Drama", "rating": 9.0, "poster_url": "https://image.tmdb.org/t/p/w500/c8Ass7acuOe4za6DhSattE359gr.jpg"},
    {"title": "A Beautiful Mind", "genre": "Drama", "rating": 8.2, "poster_url": "https://image.tmdb.org/t/p/w500/zwzWCmH72OSC9NA0ipoqw5Zjya8.jpg"},
    {"title": "Good Will Hunting", "genre": "Drama", "rating": 8.3, "poster_url": "https://image.tmdb.org/t/p/w500/v6yShBuP7Shn17Oj3QhYlrNcwyG.jpg"},
    {"title": "The Pursuit of Happyness", "genre": "Drama", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/nWty6sDOqYgA6uzFQjAL57PJE95.jpg"},
    {"title": "The Revenant", "genre": "Drama", "rating": 8.0, "poster_url": "https://image.tmdb.org/t/p/w500/fkqJJDbMrbL3PpLbI1QwpwKJz1M.jpg"},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "poster_url": "https://image.tmdb.org/t/p/w500/bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg"},
    {"title": "12 Years a Slave", "genre": "Drama", "rating": 8.1, "poster_url": "https://image.tmdb.org/t/p/w500/xdANQijuNrJaw1HA61rDccME4Tm.jpg"},
    {"title": "Joker", "genre": "Drama", "rating": 8.4, "poster_url": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "poster_url": "https://image.tmdb.org/t/p/w500/h5J4W4veyxMXDMjeNxZI46TsHOb.jpg"},
    {"title": "The Green Mile", "genre": "Drama", "rating": 8.6, "poster_url": "https://image.tmdb.org/t/p/w500/8VN7iY9KxyNvz3TzjQwnXsQ1yH1.jpg"},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "poster_url": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"},
    {"title": "The Godfather", "genre": "Drama", "rating": 9.2, "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg"},
    {"title": "American History X", "genre": "Drama", "rating": 8.5, "poster_url": "https://image.tmdb.org/t/p/w500/c2gsmSQ2Cqv8zosqKOCwRS0GFBS.jpg"},
    {"title": "The Social Network", "genre": "Drama", "rating": 7.7, "poster_url": "https://image.tmdb.org/t/p/w500/n0ybkeh7mDcutupIJeflE7YDbh1.jpg"},
    {"title": "The Grand Budapest Hotel", "genre": "Drama", "rating": 8.1, "poster_url": "https://image.tmdb.org/t/p/w500/eWdyYQreja6JGCzqHWXpWHDrrPo.jpg"},
]

# Filme in die Datenbank einfügen
for movie in movies:
    if not Movie.objects.filter(title=movie["title"]).exists():  # Verhindert Duplikate
        Movie.objects.create(**movie)

print("Neue Filme wurden erfolgreich hinzugefügt!")