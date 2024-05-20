import flask
import sirope

from model.User import User

def get_blprint():
    usr_module = flask.blueprints.Blueprint("user_blpr", __name__,
                                        url_prefix="/user",
                                        template_folder="templates",
                                        static_folder="static")
    syrp = sirope.Sirope()
    return usr_module, syrp

user_blpr, srp = get_blprint()

@user_blpr.route("/follow", methods=["POST"])
def user_follow():
    usernameFollower = flask.request.form.get("uFollow")
    usernameFollowed = flask.request.form.get("uFollowed")

    uFollower = User.find(usernameFollower)
    uFollowing = User.find(usernameFollowed)

    uFollower.addFollow(usernameFollowed)
    uFollowing.addFollower(usernameFollower)

    return flask.redirect("/viewProfile")

@user_blpr.route("/unfollow", methods=["POST"])
def user_unfollow():
    userUnfollower = flask.request.form.get("uUnfollower")
    userUnfollowed = flask.request.form.get("uUnfollowed")

    uUnfollower = User.find(userUnfollower)
    uUnfollowing = User.find(userUnfollowed)

    uUnfollower.stopFollowing(userUnfollowed)
    uUnfollowing.removeFollower(userUnfollower)

    return flask.redirect("/viewProfile")