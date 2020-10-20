import json
from error_code.error_code_list import ERROR_CODE_LIST


def generate_results(error_code=None):
    if not error_code:
        return {"SecurityCheckResult": "SUCCEED", "errorCode": None, "errorInfo": None, "data": None}
    else:
        return {"SecurityCheckResult": "FAILED", "errorCode": error_code, "errorInfo": ERROR_CODE_LIST.get(error_code),
                "data": None}


def security_check(input_data):
    if isinstance(input_data, list) or isinstance(input_data, dict):
        return generate_results()
    else:
        return generate_results("010001")


def security_check_v1(input_data):
    try:
        input_data = json.loads(input_data)
    except:
        return generate_results("010001")
    if isinstance(input_data, list) or isinstance(input_data, dict):
        return generate_results()
    else:
        return generate_results("010001")
