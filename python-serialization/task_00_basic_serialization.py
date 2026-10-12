#!/usr/bin/env python3
import json

"""file for converting and decoding data"""


def serialize_and_save_to_file(data, filename):
    """Module for saving data as a specific type"""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Function for decoding informatio"""
    with open(filename, "r") as f:
        return json.load(f)
