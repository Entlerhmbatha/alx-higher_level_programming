#!/usr/bin/python3
"""load frjson"""
import json


def load_from_json_file(filename):
    """load frofile"""
    with open(filename, encoding="utf-8") as file_loaded:
        return json.load(file+loaded)
