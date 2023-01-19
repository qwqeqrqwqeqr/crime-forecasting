create table if not exists public.congestion
(
    day_month_year  integer    not null,
    weekday         varchar(2),
    hour            varchar(4) not null,
    grid_number     varchar(6) not null,
    report_count    integer,
    life_population double precision,
    name            varchar(30),
    constraint congestion_pk
        primary key (day_month_year, grid_number, hour)
)

