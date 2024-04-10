#!/usr/bin/python3
"""
Module converts Python Objects to JSON Strings.
Output file with Object or String content is passed
to 'load' function to ensure Object type. Output is
appended to a new list. Otherwise, user passed args
are appended. The list Object is passed to the 'save'
function, converted to JSON format and saved to file.
"""

import sys
import os.path


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

new_list = []

if os.path.exists('add_item.json') and os.path.getsize('add_item.json') > 0:
    new_list = load('add_item.json')

for arg in sys.argv[1:]:
    new_list.append(arg)

save(new_list, 'add_item.json')
