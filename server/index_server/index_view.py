from flask import Blueprint, render_template

SERVER_INDEX = Blueprint("server_index", __name__)


@SERVER_INDEX.route("/index", methods=["GET"])
def post_index():
    return render_template('index.html', )


@SERVER_INDEX.route("/textComparison", methods=["GET"])
def post_text_comparison():
    return render_template('textComparison.html', )


@SERVER_INDEX.route("/jsonsort", methods=["GET"])
def post_json_sort():
    return render_template('jsonSort.html', )


@SERVER_INDEX.route("/jsonstring", methods=["GET"])
def post_json_string():
    return render_template('jsonString.html', )


@SERVER_INDEX.route("/geo", methods=["GET"])
def post_geo():
    return render_template('geo.html', )
