def json_sort(input_data):
    def dict_sort_by_key(data):
        data = sorted(data.items(), key=lambda item: item[0])
        return {item[0]: item[1] for item in data}

    if isinstance(input_data, dict):
        input_data = dict_sort_by_key(input_data)
        for k in input_data:
            if isinstance(input_data[k], dict):
                input_data[k] = dict_sort_by_key(input_data[k])
                input_data[k] = json_sort(input_data[k])
            if isinstance(input_data[k], list):
                input_data[k] = json_sort(input_data[k])

    if isinstance(input_data, list):
        for i in range(len(input_data)):
            input_data[i] = json_sort(input_data[i])

    return input_data
