from flask import Flask
from server.json_sort_server.json_sort.json_sort_api import JSON_SORT_API, JSON_SORT_V2_API
from server.json_string_server.json_string.json_string_api import JSON_STRING_API
from server.text_comparison_server.text_comparison.text_comparison_api import TEXT_COMPARISON_API
from server.identifying_animals_server.identifying_animals.identifying_animals_api import IDENTIFYING_ANIMALS_API
from server.index_server.index_view import TEXT_COMPARISON_INDEX, JSON_SORT_INDEX, JSON_STRING_INDEX

APP = Flask(__name__)
APP.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
APP.register_blueprint(JSON_SORT_API)
APP.register_blueprint(JSON_STRING_API)
APP.register_blueprint(JSON_SORT_V2_API)
APP.register_blueprint(TEXT_COMPARISON_API)
APP.register_blueprint(IDENTIFYING_ANIMALS_API)
APP.register_blueprint(TEXT_COMPARISON_INDEX)
APP.register_blueprint(JSON_SORT_INDEX)
APP.register_blueprint(JSON_STRING_INDEX)

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=9099, debug=False)
