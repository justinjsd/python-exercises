def find_movies(database: list, search_term: str):
    result = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():  # Case-insensitive search
            result.append(movie)
    return result

if __name__ == "__main__":
    database = [
        {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
        {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
        {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
    ]
    
    matching_movies = find_movies(database, "Python")
    for movie in matching_movies:
        print(movie)