import random
import string
import hmac
import hashlib


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def encode_list(item_list):
    list_val = []
    for item in item_list:
        obj_val = encode_object(item)
        list_val.append(obj_val)
    output = '&'.join(list_val)
    output = '[' + output + ']'
    return output


def encode_object(param_map):
    sorted_keys = sorted(param_map.keys())
    ret_list = []
    for key in sorted_keys:
        val = param_map[key]
        if isinstance(val, list):
            list_val = encode_list(val)
            ret_list.append(f'{key}={list_val}')
        elif isinstance(val, dict):
            # call encode_object recursively
            dict_val = encode_object(val)
            ret_list.append(f'{key}={dict_val}')
        elif isinstance(val, bool):
            bool_val = str(val).lower()
            ret_list.append(f'{key}={bool_val}')
        else:
            general_val = str(val)
            ret_list.append(f'{key}={general_val}')
    sorted_list = sorted(ret_list)
    output = '&'.join(sorted_list)
    return output


def get_signature(secret_key, api_path, param_map):
    str_to_sign = api_path + '&' + encode_object(param_map)
    sig = hmac.new(secret_key.encode('utf-8'), str_to_sign.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    return sig
