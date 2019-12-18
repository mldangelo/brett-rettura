"""Buyer's premium calculation."""
# Python Modules
from os import path
import sys
# 3rd Party Modules
import yaml

file_path = path.join(path.dirname(path.realpath(__file__)), 'buyers_premium_map.yaml')

with open(file_path, 'r') as file:
    buyers_premium_map = yaml.load(file, Loader=yaml.Loader)


if __name__ == "__main__":
    pass
