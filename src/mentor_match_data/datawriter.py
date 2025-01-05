"""This module is responsbile for writing the dummy data."""

import csv
from dataclasses import asdict, dataclass

from mentor_match_data.models import Person


@dataclass
class DataWriter:
    """Writes data associated with the program."""

    def write_people(self, people: list[Person], file_path: str) -> None:
        """Writes the people to file path."""
        with open(file_path, "w", newline="") as csvfile:
            fieldnames = [
                "first_name",
                "last_name",
                "email",
                "availability",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for p in people:
                writer.writerow(asdict(p))
