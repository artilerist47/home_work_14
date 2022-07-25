from flask import Flask

from main_views import main_blueprint, movie_blueprint, rating_blueprint, genre_blueprint, \
    search_by_year_and_type_and_genre_blueprint, search_by_actor_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(movie_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(genre_blueprint)
app.register_blueprint(search_by_year_and_type_and_genre_blueprint)
app.register_blueprint(search_by_actor_blueprint)

if __name__ == "__main__":
    app.run()
