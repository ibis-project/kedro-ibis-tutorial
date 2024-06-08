# Convert the imperial units to metric, and drop the imperial columns.
flights_metric_mutate_drop = (
    flights.mutate(distance_km=flights.distance * 1.609).drop("distance")
)

flights_metric_mutate_drop
