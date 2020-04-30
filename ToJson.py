def to_json(obj):

    if isinstance(obj, bool):
        return str(obj).lower()

    elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
        return str(obj)

    elif isinstance(obj, str):
        return '"' + obj + '"'

    elif obj is None:
        return "null"

    elif isinstance(obj, tuple) or isinstance(obj, list):
        return list_or_tuple(obj)

    elif isinstance(obj, dict):
        return dict_transform(obj)

def list_or_tuple(obj):
    json_str = "["
    len_obj = 0
    for i in obj:
        json_str += to_json(i) 
        if len_obj != len(obj) - 1:
            json_str += ", "
        len_obj += 1
    json_str += "]"
    return json_str


def dict_transform(obj):
    json_str = "{"
    len_obj = 0
    for key, value in obj.items():
        json_str += '"'+ str(key) + '": ' + to_json(value)
        if len_obj != len(obj) - 1:
            json_str += ", "
        len_obj += 1
    json_str += "}"
    return json_str
