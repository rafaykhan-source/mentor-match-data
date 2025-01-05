"""Generates a dummy dataset of people."""

import argparse

from mentor_match_data.datawriter import DataWriter
from mentor_match_data.generators import RandomPersonGenerator


def get_args() -> argparse.Namespace:
    """Returns the arguments for the program."""
    parser = argparse.ArgumentParser(
        description="This program generates the data for the mentor match application.",
    )
    parser.add_argument("n", type=int, help="The number of people to generate.")
    parser.add_argument(
        "file_path",
        type=str,
        help="The location to store generated people.",
    )
    return parser.parse_args()


def main() -> None:
    """The application entrypoint."""
    args = get_args()
    r = RandomPersonGenerator()
    people = [r.get_person() for _ in range(args.n)]

    w = DataWriter()
    w.write_people(people, args.file_path)


main()
