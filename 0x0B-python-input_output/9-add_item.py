#!/usr/bin/python3
"""
Module: that adds all arguments to a Python list, and then save them to a file:
"""


import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


data = []
args = sys.argv[1:]
if os.path.isfile("add_item.json"):
    data = load_from_json_file("add_item.json")
save_to_json_file(data + args, "add_item.json")
