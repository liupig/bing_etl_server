import json


def json_string(input_data):
    """
    Less time consuming
    :param input_data:
    :return:
    """
    input_data = json.dumps(input_data, ensure_ascii=False)

    return input_data