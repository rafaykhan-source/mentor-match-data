"""This module is reponsible creating dummy fields for dataclasses."""

import random
from dataclasses import dataclass

import names

from mentor_match_data.models import Person


@dataclass
class RandomPersonGenerator:
    """This class is responsbile for generating a Random Person ADT."""

    def __post_init__(self) -> None:
        """Adds class constants."""
        self.availability_options = self._get_availability_options()

    def _get_availability_options(self) -> list[str]:
        """Returns the availability opconstations for a person."""
        weekdays = ["M", "T", "W", "Th", "F"]
        self.availability_options = [
            f"{t}:00-{t+1}:00pm {day}" for day in weekdays for t in range(5, 9)
        ]
        self.availability_options.extend(
            [f"{t}:00-{t+1}:00pm Sun" for t in range(3, 9)],
        )

        return self.availability_options

    def _get_availability(self) -> list[str]:
        """Returns a random generated availability for a person."""
        return random.sample(
            self.availability_options,
            random.randint(3, 5),
        )

    def get_person(self) -> Person:
        """Returns a random person."""
        first, last = names.get_first_name(), names.get_last_name()
        return Person(
            first_name=first,
            last_name=last,
            email=f"{first}{last}@email.com",
            availability=self._get_availability(),
        )
