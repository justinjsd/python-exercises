# Write your solution here:

class Series:
    def __init__(self, title: str, seasons: int, genre: list):
        self.title = title
        self.seasons = seasons
        self.genre =  genre 
        self.ratings = []

    # Addings ratings for the series
    def rate(self, rating: int):
        self.ratings.append(rating)

    # Returns average rating which can be used outside the class
    def average_rating(self):
        return sum(self.ratings)/len(self.ratings)

    # Prints the output of the class as per requirement
    def __str__(self):
        genre_string = ", ".join(self.genre)
        try:
            self.num_of_rating = len(self.ratings)
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{self.num_of_rating:.0f} ratings, average {self.average_rating():.1f} points"
        except:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"

# Returns a list of series which have the minimum rating
def minimum_grade(rating: float, series_list: list):
    series_min_rating = []
    for series in series_list:
        if series.average_rating() >= rating:
            series_min_rating.append(series)
    return series_min_rating

# Returns a list of series which are the genre given
def includes_genre(genre: str, series_list: list):
    series_genre = []
    for series in series_list:
        if genre in series.genre:
            series_genre.append(series)
    return series_genre

if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)