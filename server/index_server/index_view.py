from flask import Blueprint, render_template

TEXT_COMPARISON_INDEX = Blueprint("text_comparison_index", __name__)
JSON_SORT_INDEX = Blueprint("json_sort_index", __name__)
JSON_STRING_INDEX = Blueprint("json_string_index", __name__)


@TEXT_COMPARISON_INDEX.route("/textc", methods=["GET"])
def post_poi_mapping_data():
    return render_template('index.html', )


@JSON_SORT_INDEX.route("/jsonsort", methods=["GET"])
def post_poi_mapping_data():
    return render_template('jsonSort.html', )


@JSON_STRING_INDEX.route("/jsonstring", methods=["GET"])
def post_poi_mapping_data():
    return render_template('jsonString.html', )
