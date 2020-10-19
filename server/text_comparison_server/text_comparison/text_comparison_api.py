from flask import request, Blueprint
from server.text_comparison_server.text_comparison.text_comparison_process import comparison_process

TEXT_COMPARISON_API = Blueprint("text_comparison_api", __name__)


@TEXT_COMPARISON_API.route("/v1/bing/etl/comparison", methods=["POST"])
def post_poi_mapping_data():
    main = request.form.get("main")
    sub = request.form.get("sub")
    flag = request.form.get("json_sort_flag")
    return comparison_process(main, sub, flag)
