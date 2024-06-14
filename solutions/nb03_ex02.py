def create_model_input_table(flights, weather):
    return (
        flights.mutate(
            arr_delay=flights.arr_delay >= 30,
            date=flights.time_hour.date(),
        )
        .inner_join(weather, ["origin", "time_hour"])
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
        .dropna()
    )

pipe = pipeline([
    n0,
    node(
        func=create_model_input_table,
        inputs=["preprocessed_flights", "weather"],
        outputs="model_input_table",
    ),
])
