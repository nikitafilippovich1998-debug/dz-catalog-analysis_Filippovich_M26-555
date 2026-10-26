import math

#Этап №1, Базовые функции

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    total_rating = 0
    for movie in movies:
        total_rating += movie['rating']
    medium_rating = total_rating / len(movies)
    return round(medium_rating, 1)



def catalog_age_stats(movies, current_year = 2026):
    oldest = 0
    newest = 100
    total_age = 0
    for movie in movies:
        age = current_year - movie['year']
        if age > oldest:
            oldest = age
        if age < newest:
            newest = age
        total_age += age
    medium_age = total_age / len(movies)
    medium_age = math.ceil(medium_age)
    return oldest, newest, medium_age


#print(catalog_age_stats(movies))


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f'{hours} ч {mins} м'


#print(duration_in_hours(155))


#Этап №2 Условия и match


def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    elif rating >= 5:
        return 'средне' if rating >= 5 else 'слабо'
    else:
        return 'слабо'


def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if year >= 2015:
            return 'недавние'
        case _:
            return 'старые'

#print(rating_tier(8.5))
#print(decade_label(2018))


def print_non_comedies(movies):
    for movie in movies:
        if 'comedy' in movie['genres']:
            continue
        print(movie['title'])


def find_masterpiece(movies):
    index = 0
    while index < len(movies):
        if movies [index]['rating'] > 9.0:
            print(f'Найден шедевр: {movies[index]['title']}')
            break
        index += 1
    else:
        print('Шедевров не найдено')


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie ['duration_min'] > threshold:
            count += 1
    return count


#print('--- Проверка Этапа 3 ---')
#print_non_comedies(movies)
#find_masterpiece(movies)
#print(count_long_movies(movies))

#Этап №4 Строки


def normalize_title(title):
    words = title.split()
    result = []
    for word in words:
        capitalized_word = word[0].upper() + word[1:]
        result.append(capitalized_word)
    return " ".join(result)


def make_slug(title):
    normalized = normalize_title(title) 
    lower_title = normalized.lower()
    return lower_title.replace(' ', '-')


def format_report_line(movie):
    year = movie["year"]
    rating = movie["rating"]
    title = normalize_title( movie['title'])
    duration = duration_in_hours (movie["duration_min"])
    genres = ",".join(sorted (movie["genres"]))
    return f'"{title}" ({year}) - {rating}/10, {duration}, жанры: {genres}'


#print(normalize_title("silent hours"))
#print(make_slug("The Quiet Algorithm"))
#print(format_report_line(movies[5]))


#Этап №5, Списки


def titles_sorted_by_rating(movies):
    sorted_movies = sorted (movies, key=lambda movie: movie["rating"], reverse=True)

    result = []
    for movie in sorted_movies:
        result.append(normalize_title(movie["title"]))
    return result


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    top_movies = sorted_movies[:n]

    result = []
    for movie in top_movies:
        movie_tuple = (normalize_title(movie["title"]), movie["rating"])
        result.append(movie_tuple)
    return result


#print(titles_sorted_by_rating(movies))
#print(top_n_by_rating(movies, 3))


#Этап №6, Словари


def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie['genres']:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        title = normalize_title(movie["title"])
        for actor in movie["actors"]:
            actor_movies = filmography.get(actor, [])
            actor_movies.append(title)
            filmography[actor] = actor_movies
    return filmography


def high_rated_movies(movies):
    avg_rating = average_rating(movies)
    return {normalize_title(movie["title"]): movie["rating"]
            for movie in movies
            if movie["rating"] > avg_rating}


print(count_by_genre(movies))
print(actor_filmography(movies))
print(high_rated_movies(movies))
