from flask import Flask
from json_sort_server.json_sort.json_sort_api import JSON_SORT_API

APP = Flask(__name__)
APP.register_blueprint(JSON_SORT_API)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=9099, debug=True)