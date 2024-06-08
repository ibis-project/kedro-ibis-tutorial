# Which airlines had the longest average arrival delays in June 2013?
sol2 = (
    flights.filter(
        [
            flights.month == 6,
            flights.year == 2013,
        ]
    )
    .group_by("carrier")
    .agg(average_arr_delay=flights.arr_delay.try_cast(int).mean())
    .order_by(ibis.desc("average_arr_delay"))
)

sol2
