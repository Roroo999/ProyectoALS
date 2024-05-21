import flask
import sirope

from model.User import User
from model.Post import Post

def get_blprint():
    usr_module = flask.blueprints.Blueprint("user_blpr", __name__,
                                        url_prefix="/user",
                                        template_folder="templates",
                                        static_folder="static")
    syrp = sirope.Sirope()
    return usr_module, syrp

user_blpr, srp = get_blprint()

@user_blpr.route("/searchUser", methods=["POST"])
def search_user():
    
    searchUser = flask.request.form.get('searchQuery').lower()

    res = srp.find_first(User, lambda u: u.username == searchUser)

    user = User.current_user()

    if res is not None:
        recent_posts = srp.filter(Post, lambda p: p.user == res.username)
        followed = 0
        if res.username in user.followed:
            followed = 1

        sust = {"username" : res.username,
                "followers" : len(res.followers),
                "following" : len(res.followed),
                "followed" : followed, 
                "recent_posts" : list(recent_posts)}
        return flask.render_template("profile.html", **sust)
    else:
        flask.flash("User not found!")
        return flask.redirect("/home/main")

@user_blpr.route("/follow", methods=["POST"])
def user_follow():

    usernameFollowed = flask.request.form.get("uFollowed")

    uFollower = User.current_user()
    uFollowing = User.find(usernameFollowed)

    uFollower.addFollow(usernameFollowed)
    uFollowing.addFollower(uFollower.username)

    return flask.redirect("/viewProfile")

@user_blpr.route("/unfollow", methods=["POST"])
def user_unfollow():
    userUnfollowed = flask.request.form.get("uUnfollowed")

    uUnfollower = User.current_user()
    uUnfollowing = User.find(userUnfollowed)

    uUnfollower.stopFollowing(userUnfollowed)
    uUnfollowing.removeFollower(uUnfollower.username)

    return flask.redirect("/viewProfile")