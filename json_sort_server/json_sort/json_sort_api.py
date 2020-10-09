import json
from flask import request, Blueprint
from json_sort_server.json_sort.json_sort_process import json_sort, json_sort_simple
from json_sort_server.json_sort.input_check import security_check

JSON_SORT_API = Blueprint("json_sort_api", __name__)


@JSON_SORT_API.route(f"/v1/bing/etl/jsonsort", methods=["POST"])
def post_poi_mapping_data():
    request_data = request.get_json()
    check_result = security_check(request_data)
    if check_result.get("SecurityCheckResult") == "SUCCEED":
        check_result["data"] = json_sort(request_data)
        # or
        # check_result["data"] = json_sort_simple(request_data)
        return check_result
    else:
        return check_result
