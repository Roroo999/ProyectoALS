import flask
import json
import flask_login
import sirope
from model.User import User

from views.user import user_blpr
from views.dashboard import dash_blpr

def create_app():
    lmanager = flask_login.login_manager.LoginManager()
    fapp = flask.Flask(__name__)
    syrp = sirope.Sirope()
    fapp.config.from_file("config.json", load=json.load)
    lmanager.init_app(fapp)
    fapp.register_blueprint(user_blpr)
    fapp.register_blueprint(dash_blpr)

    return fapp, lmanager, syrp

app, lm, srp = create_app()

@app.route("/", methods=["GET"])
def main():
    sust = {}
    return flask.render_template("login.html", **sust)

@app.route("/login", methods=["POST"])
def login():
    username = flask.request.form.get("username").lower()
    passwd = flask.request.form.get("passwd")
    user = User.find(srp, username)
    
    if user is not None:
        if user.compare_passwd(passwd):
            flask_login.login_user(user)
            return flask.redirect("/home/main")
        else:
            flask.flash("Error: las credenciales no coinciden")
            return flask.redirect("/")
    else:
        flask.flash("Error: el usuario no existe")
        return flask.redirect("/")



@app.route("/register", methods=["GET"])
def register():
    sust = {}
    return flask.render_template("register.html", **sust)

@app.route("/register", methods=["POST"])
def createUser():

    username = flask.request.form.get("username")
    email = flask.request.form.get("email")
    passwd = flask.request.form.get("passwd")

    if(User.find(srp, username) == None ):
        srp.save(User(username, email, passwd))
        return flask.redirect("/")
    else:
        flask.flash("Error: el nombre de usuario no esta disponible")
        return flask.redirect("/register")
    
@app.route("/logout")
def logout():
    flask_login.logout_user()
    return flask.redirect("/")
    


@lm.user_loader
def user_loader(username):
    return User.find(srp, username)

@lm.unauthorized_handler
def unauthorized_handler():
    flask.flash("Unauthorized")
    return flask.redirect("/")

if __name__ == "__main__":
    app.run()
