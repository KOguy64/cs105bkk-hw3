"""HW3 · walks.py: read the step counter's CSV file and keep only the good rows. Practises
Session 7 (reading a CSV file, cleaning data) and Session 9 (a generator and a decorator).
"""

import csv
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Walk:
    """Provided: one walk from the log, cleaned. `steps` is a whole number, 0 or more."""

    date: str
    steps: int
    place: str


def parse_walk(row: dict[str, str]) -> Walk:
    """Turn one row of the CSV file into a Walk, or raise ValueError if the row is bad."""
    date = row["date"].strip()
    if not date:
        raise ValueError("Date is unparsable")

    steps = row["steps"]
    try:
        if float(int(steps)) != float(steps):
            raise ValueError
        steps = int(steps)
        if steps < 0:
            raise ValueError
    except:
        raise ValueError(f"{steps} is unparsable")

    place = row["place"].strip()
    return Walk(date, steps, place)


def none_on_error(func: Callable) -> Callable:
    """A decorator: the wrapped function returns None instead of raising ValueError."""

    def pcall(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return None

    return pcall


def read_rows(path: Path) -> Iterator[dict[str, str]]:
    """Yield the rows of a CSV file one at a time, each as a dict of text."""
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            yield row


def good_walks(rows: Iterable[dict[str, str]]) -> Iterator[Walk]:
    """Yield a Walk for every good row, one at a time, and skip the bad rows."""
    for row in rows:
        parse = none_on_error(parse_walk)(row)
        if parse:
            yield parse
