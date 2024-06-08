# Which NYC airport has the lowest percentage of outbound flights
# arriving 30 or more minutes late?
sol3 = (
    flights.group_by("origin")
    .agg((flights.arr_delay.try_cast(int) >= 30).mean())
    .order_by("Mean(GreaterEqual(TryCast(arr_delay, Int64), 30))")
)

sol3
