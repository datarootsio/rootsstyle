""" This script adds information about a new release to the CHANGELOG.md file.
Two arguments are passed:
    str: The changes made in the new version
"""
import argparse

LOG_FILE = "CHANGELOG.md"


def read_current_changelog():
    with open(LOG_FILE, "r") as f:
        return f.read()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("changes", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    current_changelog = read_current_changelog()

    new_changelog = f"{args.changes}\n{current_changelog}"
    with open(LOG_FILE, "w") as f:
        f.write(new_changelog)
