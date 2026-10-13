#!/usr/bin/env python3
"""Module for converting csv to json"""

import csv
import json


def convert_csv_to_json(filename):
    """Function for converting csv to json"""
    try:
        with open(filename, "r") as f:
            data = list(csv.DictReader(f))

        with open("data.json", "w") as j:
            json.dump(data, j, indent=4)
            return True
    except (OSError, EOFError):
        return False
