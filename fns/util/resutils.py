import json
import os

from definitions import ROOT_DIR
from fns.constant.path import Paths
from fns.util.pathutils import append_file_name


def get_api_key():
    key_file_path = append_file_name(ROOT_DIR, Paths.Resources.NewsAPI.get_api_key_file_path())

    if not os.path.exists(key_file_path):
        raise Exception("NewsAPI key file does not exist under path: {}".format(key_file_path))

    with open(key_file_path, "r") as fin:
        api_json = json.load(fin)

    return api_json["key"]


def get_category_maps(path: str=Paths.Resources.get_default_category_maps()):
    category_map_path = append_file_name(ROOT_DIR, path)
    with open(category_map_path, "r") as fin:
        return json.load(fin)


def get_database_paths():
    database_paths_path = append_file_name(ROOT_DIR, Paths.Resources.get_database_paths())

    with open(database_paths_path, "r") as fin:
        return json.load(fin)
