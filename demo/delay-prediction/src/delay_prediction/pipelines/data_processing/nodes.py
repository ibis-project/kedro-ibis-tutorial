from __future__ import annotations

from typing import TYPE_CHECKING

import ibis.selectors as s
from ibis import _

if TYPE_CHECKING:
    import ibis.expr.types as ir


def _replace_na_values(t: ir.Table) -> ir.Table:
    return t.mutate(s.across(s.of_type("string"), _.nullif("NA")))


def preprocess_flights(flights: ir.Table) -> ir.Table:
    """Preprocesses the data for flights.

    Args:
        flights: Raw data.
    Returns:
        Preprocessed data, with `dep_time` converted to a time and
        `arr_delay` and `air_time` converted to integers.
    """
    return _replace_na_values(flights).mutate(
        dep_time=(
            _.dep_time.lpad(4, "0").substr(0, 2)
            + ":"
            + _.dep_time.substr(-2, 2)
            + ":00"
        ).cast("time"),
        arr_delay=_.arr_delay.cast(int),
        air_time=_.air_time.cast(int),
    )


def create_model_input_table(flights: ir.Table, weather: ir.Table) -> ir.Table:
    """Combines all data to create a model input table.

    Args:
        flights: Preprocessed data for flights.
        weather: Raw data for weather.
    Returns:
        Model input table.
    """
    return (
        flights.mutate(
            # Convert the arrival delay to a factor
            arr_delay=flights.arr_delay >= 30,
            # We will use the date (not date-time) in the recipe below
            date=flights.time_hour.date(),
        )
        # Include the weather data
        .inner_join(weather, ["origin", "time_hour"])
        # Only retain the specific columns we will use
        .select(
            "dep_time",
            "flight",
            "origin",
            "dest",
            "air_time",
            "distance",
            "carrier",
            "date",
            "arr_delay",
            "time_hour",
        )
        # Exclude missing data
        .dropna()
    )
