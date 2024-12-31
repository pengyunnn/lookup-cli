#!/usr/bin/env python3

import os
import sys
import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def lookup(name, output_field, data):
    for person in data:
        if person.get("name") == name:
            return person.get(output_field, "Field not found")
    return "Name not found"

def main():
    if len(sys.argv) < 2:
        print("Usage: lookup-cli <name> [<output_field>]")
        sys.exit(1)

    file_path = os.environ.get("YAML_FILE_PATH")
    name = sys.argv[1]
    output_field = sys.argv[2] if len(sys.argv) > 2 else None

    data = read_yaml(file_path)

    if output_field:
        print(lookup(name, output_field, data))
    else:
        print("Usage: lookup-cli <name> [<output_field>]")

if __name__ == "__main__":
    main()
