import json


def json_string(input_data, flag):
    """
    Less time consuming
    :param input_data:
    :return:
    """
    if flag == "true":
        input_data = json.dumps(input_data, ensure_ascii=False, separators=(',', ':'))
    else:
        input_data = json.dumps(input_data, ensure_ascii=False)

    return input_data
