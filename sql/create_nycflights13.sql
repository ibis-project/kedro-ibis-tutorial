DROP TABLE IF EXISTS flights CASCADE;
CREATE TABLE flights (
    "year" BIGINT,
    "month" BIGINT,
    "day" BIGINT,
    "dep_time" VARCHAR,
    "sched_dep_time" BIGINT,
    "dep_delay" VARCHAR,
    "arr_time" VARCHAR,
    "sched_arr_time" BIGINT,
    "arr_delay" VARCHAR,
    "carrier" VARCHAR,
    "flight" BIGINT,
    "tailnum" VARCHAR,
    "origin" VARCHAR,
    "dest" VARCHAR,
    "air_time" VARCHAR,
    "distance" BIGINT,
    "hour" BIGINT,
    "minute" BIGINT,
    "time_hour" TIMESTAMP(6)
);

DROP TABLE IF EXISTS weather CASCADE;
CREATE TABLE weather (
    "origin" VARCHAR,
    "year" BIGINT,
    "month" BIGINT,
    "day" BIGINT,
    "hour" BIGINT,
    "temp" VARCHAR,
    "dewp" VARCHAR,
    "humid" VARCHAR,
    "wind_dir" VARCHAR,
    "wind_speed" VARCHAR,
    "wind_gust" VARCHAR,
    "precip" DOUBLE PRECISION,
    "pressure" VARCHAR,
    "visib" DOUBLE PRECISION,
    "time_hour" TIMESTAMP(6)
);
