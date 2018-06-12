import json

from fns.path import Paths


def get_api_key():
    with open(Paths.NewsAPI.key_file, "r") as fin:
        api_json = json.load(fin)

    return api_json["key"]
