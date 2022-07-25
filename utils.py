import sqlite3


def get_data_by_db(query):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(query)

        return result


def search_by_title(title):
    query = f"""
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title LIKE '{title}'
            ORDER BY release_year DESC
            """

    result = get_data_by_db(query)

    for i in result:
        return dict(i)


def search_by_release_year(year_from, year_before):
    query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN '{year_from}' AND '{year_before}'
            LIMIT 100
            """

    result = get_data_by_db(query)

    titles_by_year = []
    for i in result:
        titles_by_year.append(dict(i))

    return titles_by_year


def search_by_rating(rating):
    if rating == "children":
        query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G'
                    """

    elif rating == "family":
        query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
                """

    elif rating == "adult":
        query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating = 'R' OR rating = 'NC-17'
                """

    result = get_data_by_db(query)

    titles_by_rating = []
    for i in result:
        titles_by_rating.append(dict(i))

    return titles_by_rating


def search_by_genre(genre):
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
            """

    result = get_data_by_db(query)

    titles_by_genre = []
    for i in result:
        titles_by_genre.append(dict(i))

    return titles_by_genre


def search_by_year_and_type_and_genre(release_year, type_, genre):
    query = f"""
            SELECT title
            FROM netflix
            WHERE listed_in LIKE '%{genre}%' AND release_year = '{release_year}' AND "type" = '{type_}'
            """

    result = get_data_by_db(query)
    print(result)

    titles_by_genre = []
    for i in result:
        titles_by_genre.append(dict(i))

    return titles_by_genre


def search_by_actor(name_one, name_two):
    query = f"""
            SELECT "cast"
            FROM netflix
            WHERE "cast" like '%{name_one}%' AND "cast" LIKE '%{name_two}%'
            """

    result = get_data_by_db(query)

    double_actors = []

    actors = {}
    for actor in result:
        names = set(dict(actor).get("cast").split(",")) - set([name_one, name_two])

        for name in names:
            actors[str(name).strip()] = actors.get(str(name).strip(), 0) + 1

    for keys, values in actors.items():
        if values >= 2:
            print(keys)
            double_actors.append(keys)

    return double_actors
