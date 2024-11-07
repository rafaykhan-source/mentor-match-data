"""Generates a dummy dataset of people."""

import argparse
import csv
from dataclasses import asdict

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
    with open(args.file_path, "w", newline="") as csvfile:
        fieldnames = [
            "first_name",
            "last_name",
            "email",
            "availability",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(args.n):
            writer.writerow(asdict(r.get_person()))


main()
