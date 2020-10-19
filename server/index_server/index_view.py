from flask import Blueprint, render_template

INDEX = Blueprint("index", __name__)


@INDEX.route("/index", methods=["GET"])
def post_poi_mapping_data():
    return render_template('index.html', )
