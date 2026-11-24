"""Part 10: your own tests for parse_walk. The README says what to write here.

We grade this file by running it against a correct walks.py, where every test must pass,
and against versions of walks.py with a bug planted in parse_walk, where your tests should fail.
"""

import copy

import pytest
from walks import Walk, parse_walk


@pytest.fixture
def good_row() -> dict[str, str]:
    """Provided: one good row, as csv.DictReader gives it. Each test gets its own new copy."""
    return {"date": "2026-11-16", "steps": "4200", "place": "Lumphini Park"}


def test_core_example_a_good_row_becomes_a_walk(good_row):
    """Provided: an example that uses the fixture. Write your own tests below it."""
    assert parse_walk(good_row) == Walk("2026-11-16", 4200, "Lumphini Park")


# Your tests go here.
@pytest.mark.parametrize("date", ["", " ", "   "])
def test_core_date_cant_be_empty(good_row, date):
    good_row["date"] = date
    with pytest.raises(ValueError):
        parse_walk(good_row)


@pytest.mark.parametrize("steps", ["abc", "12.5", "-100", "-1", "", "    "])
def test_core_steps_are_checked(good_row, steps):
    good_row["steps"] = steps
    with pytest.raises(ValueError):
        parse_walk(good_row)


def test_0_is_good_row(good_row):
    good_row["steps"] = "0"
    assert parse_walk(good_row) == Walk("2026-11-16", 0, "Lumphini Park")


@pytest.mark.parametrize("key", ["steps", "date", "place"])
def test_good_rows_are_trimmed(good_row, key):
    good_row[key] = "   " + good_row[key] + "  "

    assert parse_walk(good_row) == Walk("2026-11-16", 4200, "Lumphini Park")


@pytest.mark.parametrize("key", ["steps", "date", "place"])
def test_rows_arent_changed(good_row, key):
    good_row[key] = "   " + good_row[key] + "  "
    other_row = copy.deepcopy(good_row)

    parse_walk(good_row)
    assert other_row == good_row
