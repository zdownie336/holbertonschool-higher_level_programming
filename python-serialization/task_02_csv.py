#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    with open(filename, "r") as f:
        data = list(csv.DictReader(f))

    with open("data.json", "w") as j:
        file = json.dump(data, j, indent=4)
        return file
