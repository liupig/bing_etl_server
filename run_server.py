from flask import Flask
from server.json_sort_server.json_sort.json_sort_api import JSON_SORT_API
from server.json_string_server.json_string.json_string_api import JSON_STRING_API
from server.text_comparison_server.text_comparison.text_comparison_api import TEXT_COMPARISON_API
from server.statutory_holiday_server.statutory_holiday.statutory_holiday_api import STATUTORY_HOLIDAY_API
from server.geohash_server.geohash.geo_api import GEO_API
from server.index_server.index_view import SERVER_INDEX

APP = Flask(__name__)
APP.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
APP.register_blueprint(JSON_SORT_API)
APP.register_blueprint(JSON_STRING_API)
APP.register_blueprint(TEXT_COMPARISON_API)
APP.register_blueprint(STATUTORY_HOLIDAY_API)
APP.register_blueprint(GEO_API)
APP.register_blueprint(SERVER_INDEX)

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=9099, debug=False)
