# Convert the imperial units to metric, and drop the imperial columns.
flights_metric_select = flights.select(
    "year",
    "month",
    "day",
    "dep_time",
    "sched_dep_time",
    "dep_delay",
    "arr_time",
    "sched_arr_time",
    "arr_delay",
    "carrier",
    "flight",
    "tailnum",
    "origin",
    "dest",
    "air_time",
    "hour",
    "minute",
    "time_hour",
    distance_km=flights.distance * 1.609,
)

flights_metric_select
