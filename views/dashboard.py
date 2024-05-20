import flask
import sirope
import random

from flask_login import current_user
from model.User import User
from model.Song import Song
from model.Lyric import Lyric
from model.Post import Post

def get_blprint():
    dash_module = flask.blueprints.Blueprint("dash_blpr", __name__,
                                        url_prefix="/home",
                                        template_folder="templates",
                                        static_folder="static")
    syrp = sirope.Sirope()
    return dash_module, syrp

dash_blpr, srp = get_blprint()

@dash_blpr.route("/main", methods=["GET"])
def show_dash():

    username = current_user.username

    post_list = get_relevant_posts()

    sust = {"post_list" : post_list}
    return flask.render_template("dashboard.html", **sust)

def get_relevant_posts():
    user = User.current_user()

    if not user:
        return []

    # Obtener publicaciones de usuarios seguidos
    followed_users = user.followed
    posts = []

    for followed_user in followed_users:
        followed_user_posts = srp.find_all(Post, lambda p: p.user == followed_user)
        posts.extend(followed_user_posts)

    # Añadir publicaciones populares (por rating)
    popular_posts = srp.find_all(Post, lambda p: p.rating > 4.0)
    posts.extend(popular_posts)

    # Filtrar y ordenar las publicaciones por relevancia
    posts = list(set(posts))  # Eliminar duplicados
    posts.sort(key=lambda p: p.rating, reverse=True)

    # Limitar el número de publicaciones para el dashboard
    max_posts = 20
    relevant_posts = posts[:max_posts]

    # Si no hay suficientes publicaciones, añadir publicaciones aleatorias
    if len(relevant_posts) < max_posts:
        all_posts = srp.find_all(Post)
        random_posts = random.sample(all_posts, max_posts - len(relevant_posts))
        relevant_posts.extend(random_posts)

    return relevant_posts