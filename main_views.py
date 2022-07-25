from flask import Blueprint, jsonify, abort

from utils import search_by_title, search_by_release_year, search_by_rating, search_by_genre, \
    search_by_year_and_type_and_genre, search_by_actor

movie_blueprint = Blueprint("movie_blueprint", __name__)


@movie_blueprint.get("/movie/<title>")
def search_by_title_view(title):
    result = search_by_title(title)
    if result is None:
        return abort(404, ValueError("No such film found|Такой фильм не найден"))
    else:
        return jsonify(result)


@movie_blueprint.get("/movie/<int:year_from>/to/<int:year_before>")
def search_by_release_year_view(year_from, year_before):
    result = search_by_release_year(year_from, year_before)
    return jsonify(result)


@movie_blueprint.get("/rating/<rating>")
def search_by_rating_view(rating):
    result = search_by_rating(rating)
    return jsonify(result)


@movie_blueprint.get("/genre/<genre>")
def search_by_genre_view(genre):
    result = search_by_genre(genre)
    return jsonify(result)


@movie_blueprint.get("/search/<release_year>/<type_>/<genre>")
def search_by_year_and_type_and_genre_view(release_year, type_, genre):
    result = search_by_year_and_type_and_genre(release_year, type_, genre)
    return jsonify(result)


@movie_blueprint.get("/search/<name_one>/<name_two>")
def search_by_actor_view(name_one, name_two):
    result = search_by_actor(name_one, name_two)
    return jsonify(result)
