import flask
import sirope

from model.User import User
from model.Song import Song
from model.Lyric import Lyric

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

    quote_list = ["donde tan las gatas que no hablan y tiran palante", "ella se adueña del lugar"]

    sust = {"quote_list" : quote_list}
    return flask.render_template("dashboard.html", **sust)
