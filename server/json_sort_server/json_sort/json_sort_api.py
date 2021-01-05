from flask import request, Blueprint
from server.json_sort_server.json_sort.json_sort_process import json_sort
from server.json_sort_server.json_sort.input_check import security_check, security_check_v1
import json

JSON_SORT_API = Blueprint("json_sort_api", __name__)
JSON_SORT_V2_API = Blueprint("json_sort_v2_api", __name__)


@JSON_SORT_API.route("/v1/bing/etl/jsonsort", methods=["POST"])
def post_json_sort():
    main = request.form.to_dict().get("main")
    if "'" in main and '"' not in main:
        main = main.replace("'", '"')
    elif "'" in main and '"' in main:
        if main.index('"', 1) > main.index("'", 1) and "_import_" not in main and "_from_" not in main:
            main = json.dumps(eval(main))

    check_result = security_check_v1(main)

    if check_result.get("SecurityCheckResult") == "SUCCEED":
        request_data = json.loads(main)
        check_result["data"] = json.dumps(json_sort(request_data), indent=4, ensure_ascii=False) if main else main
        return check_result
    else:
        return check_result


@JSON_SORT_V2_API.route("/v1/bing/etl/jsonsortapi", methods=["POST"])
def post_json_sort_v2():
    request_data = request.get_json()
    check_result = security_check(request_data)
    if check_result.get("SecurityCheckResult") == "SUCCEED":
        check_result["data"] = json_sort(request_data)
        # check_result["data"] = json_sort_simple(request_data)
        return check_result
    else:
        return check_result
