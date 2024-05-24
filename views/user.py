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
        if res.username in user.followed and res.username != user.username:
            followed = 1

        elif res.username == user.username:
            followed = -1
        
        sust = {"username" : res.username,
                "description": res.description,
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
    print("Ufollowed: " + usernameFollowed)
    uFollower = User.current_user()
    uFollowing = User.find(srp, usernameFollowed)

    uFollower.addFollow(usernameFollowed)
    uFollowing.addFollower(uFollower.username)

    srp.save(uFollowing)
    srp.save(uFollower)

    recent_posts = srp.filter(Post, lambda p: p.user == uFollowing.username)
    followed = 0
    if uFollowing.username in uFollower.followed:
        followed = 1

    sust = {"username" : uFollowing.username,
                "description": uFollowing.description,
                "followers" : len(uFollowing.followers),
                "following" : len(uFollowing.followed),
                "followed" : followed, 
                "recent_posts" : list(recent_posts)}

    return flask.render_template("profile.html", **sust)

@user_blpr.route("/unfollow", methods=["POST"])
def user_unfollow():
    userUnfollowed = flask.request.form.get("uUnfollowed")

    uUnfollower = User.current_user()
    uUnfollowing = User.find(srp, userUnfollowed)

    uUnfollower.stopFollowing(userUnfollowed)
    uUnfollowing.removeFollower(uUnfollower.username)

    srp.save(uUnfollowing)
    srp.save(uUnfollower)

    recent_posts = srp.filter(Post, lambda p: p.user == uUnfollowing.username)
    followed = 0
    if uUnfollowing.username in uUnfollower.followed:
        followed = 1

    sust = {"username" : uUnfollowing.username,
                "description": uUnfollowing.description,
                "followers" : len(uUnfollowing.followers),
                "following" : len(uUnfollowing.followed),
                "followed" : followed, 
                "recent_posts" : list(recent_posts)}

    return flask.render_template("profile.html", **sust)

@user_blpr.route("/edit_profile", methods=["GET"])
def showEditProfile():
    user = User.current_user()

    recent_posts = srp.filter(Post, lambda p: p.user == user.username)

    sust = {"username" : user.username,
                "description": user.description,
                "followers" : len(user.followers),
                "following" : len(user.followed),
                "followed" : -1, 
                "recent_posts" : list(recent_posts),
                "email" : user.email}
    
    return flask.render_template("profile.html", **sust)

@user_blpr.route("/edit_profile", methods=["POST"])
def editProfile():
    user = User.current_user()

    recent_posts = srp.filter(Post, lambda p: p.user == user.username)

    newDesc = flask.request.form.get("newDesc")
    newEmail = flask.request.form.get("newEmail")

    if newDesc is not "":
        user.description = newDesc

    if newEmail is not "":
        user.email = newEmail

    srp.save(user)

    sust = {"username" : user.username,
                "description": user.description,
                "followers" : len(user.followers),
                "following" : len(user.followed),
                "followed" : -1, 
                "recent_posts" : list(recent_posts),
                "email" : user.email}
    
    return flask.render_template("profile.html", **sust)