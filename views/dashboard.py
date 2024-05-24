import flask
import sirope

from model.User import User
from model.Song import Song
from model.Comment import Lyric
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

    user = User.current_user()
    post_list = get_relevant_posts()

    for post in post_list:
        if post.postId in user.likedPosts:
            post.liked = 1
        else:
            post.liked = 0

    sust = {"post_list" : post_list}
    return flask.render_template("dashboard.html", **sust)

@dash_blpr.route("/newPost", methods=["POST"])
def publish_post():

    songName = flask.request.form.get('songName').lower()
    songArtist = flask.request.form.get('songArtist').lower()
    songLink = flask.request.form.get('songLink')
    lyricText = flask.request.form.get('lyricText')
    lyricSinger = flask.request.form.get('lyricSinger')
    postCaption = flask.request.form.get('postCaption')

    song = Song(songName, songArtist, songLink)
    user = User.current_user()

    temp = srp.find_first(Song, lambda s: s.name == songName and s.artist == songArtist)

    #para evitar tener canciones repetidas, esto se puede utilizar para funcionalidades en un futuro
    #como mejor recomendacion de canciones segun los gustos del usuario
    if temp is None:
        srp.save(song)

    idPost = (srp.num_objs(Post) + 1)
    srp.save(Post(idPost, user.username, song.get_id(), lyricText, lyricSinger, postCaption))
    return flask.redirect("/home/main")

def get_relevant_posts():
    user = User.current_user()

    if not user:
        return []

    # Obtener publicaciones de usuarios seguidos
    followed_users = user.followed
    posts = []

    for followed_user in followed_users:
        followed_user_posts = list(srp.filter(Post, lambda p: p.user == followed_user))
        posts.extend(followed_user_posts)

    # Limitar el número de publicaciones para el dashboard
    max_posts = 20
    relevant_posts = posts[:max_posts]

    # Añadir posts de gente que no se siga pero que puedan resultar interesantes para el usuario

    return relevant_posts