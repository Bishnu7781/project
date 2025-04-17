# main.py

movies = {
    'Action': {
        '80s': "Die Hard",
        '90s': "Terminator 2",
        '2000s': "Gladiator",
        '2010s': "Mad Max: Fury Road"
    },
    'Comedy': {
        '80s': "Ghostbusters",
        '90s': "Groundhog Day",
        '2000s': "Superbad",
        '2010s': "The Grand Budapest Hotel"
    },
    'Drama': {
        '80s': "Rain Man",
        '90s': "The Shawshank Redemption",
        '2000s': "A Beautiful Mind",
        '2010s': "The Social Network"
    },
    'Sci-Fi': {
        '80s': "Blade Runner",
        '90s': "The Matrix",
        '2000s': "Minority Report",
        '2010s': "Inception"
    }
}

def get_recommendation(genre, decade):
    try:
        return movies[genre][decade]
    except KeyError:
        return None