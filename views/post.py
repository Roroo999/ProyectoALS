import flask
import sirope

from model.User import User
from model.Post import Post
from model.Comment import Comment

def get_blprint():

    post_module = flask.blueprints.Blueprint("post_blpr", __name__,
                                        url_prefix="/post",
                                        template_folder="templates",
                                        static_folder="static")
    syrp = sirope.Sirope()
    return post_module, syrp

post_blpr, srp = get_blprint()

@post_blpr.route("/like")
def likepost():

    user = User.current_user()
    userProf = flask.request.form.get("userProf")
    postId = flask.request.form.get("postID")
    post = srp.find_first(lambda p: p.postId == postId)
    post.likePost()
    user.addLikedPost(postId)
    srp.save(post)
    srp.save(user)

    if userProf != "":
        sust = getValues(user, userProf)
        return flask.render_template("profile.html", **sust)
    
    else:
        return flask.redirect("/home/main")

@post_blpr.route("/unlike")
def unlikepost():

    user = User.current_user()
    userProf = flask.request.form.get("userProf")
    postId = flask.request.form.get("postID")
    post = srp.find_first(lambda p: p.postId == postId)
    post.removeLike()
    user.removeLike(postId)
    srp.save(post)
    srp.save(user)

    if userProf != "":
        sust = getValues(user, userProf)
        return flask.render_template("profile.html", **sust)
    
    else:
        return flask.redirect("/home/main")

@post_blpr.route("/comment")
def commentpost():

    userProf = flask.request.form.get("userProf")
    
    commentText = flask.request.form.get("comment")
    postId = flask.request.form.get("postID")

    post = srp.find_first(lambda p: p.postId == postId)
    comment = Comment(User.current_user().username), post, commentText
    post.addComment(comment)

    srp.save(post)

    if userProf != "":
        sust = getValues(User.current_user(), userProf)
        return flask.render_template("profile.html", **sust)
    
    else:
        return flask.redirect("/home/main")


def getValues(user, userProf):
    res = srp.find_first(User, lambda u: u.username == userProf)

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
    return sust