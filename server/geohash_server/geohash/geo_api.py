from flask import request, Blueprint
from server.geohash_server.geohash.geohash_process import geo_decode, geo_encode
from server.geohash_server.geohash.input_check import security_check_decode, security_check_encode

import json

GEO_API = Blueprint("geo_api", __name__)


@GEO_API.route("/v1/bing/etl/geo_decode", methods=["POST"])
def post_geo_decode():
    geohash = request.form.to_dict().get("decode")
    check_result = security_check_decode(geohash)
    if check_result.get("SecurityCheckResult") == "SUCCEED":
        check_result["data"] = json.dumps(geo_decode(geohash.strip()))
        return check_result
    else:
        return check_result


@GEO_API.route("/v1/bing/etl/geo_encode", methods=["POST"])
def post_geo_encode():
    latitudel_longitude = request.form.to_dict().get("encode")
    check_result = security_check_encode(latitudel_longitude)
    if check_result.get("SecurityCheckResult") == "SUCCEED":
        latitudel_longitude = json.loads(latitudel_longitude)
        check_result["data"] = geo_encode(latitudel_longitude)
        return check_result
    else:
        return check_result

