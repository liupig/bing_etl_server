from flask import request, Blueprint
from server.json_string_server.json_string.json_sting_process import json_string
from server.json_string_server.json_string.input_check import security_check, security_check_v1
import json

JSON_STRING_API = Blueprint("json_string_api", __name__)


@JSON_STRING_API.route("/v1/bing/etl/jsonstring", methods=["POST"])
def post_poi_mapping_data():
    main = request.form.to_dict().get("main")
    if "'" in main and '"' not in main:
        main = main.replace("'", '"')
    elif "'" in main and '"' in main:
        if main.index('"', 1) > main.index("'", 1) and "_import_" not in main and "_from_" not in main:
            main = json.dumps(eval(main))

    check_result = security_check_v1(main)

    if check_result.get("SecurityCheckResult") == "SUCCEED":
        request_data = json.loads(main)
        check_result["data"] = json_string(request_data) if main else None
        return check_result
    else:
        return check_result

