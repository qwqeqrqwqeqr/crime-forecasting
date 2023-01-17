create table if not exists public.congestion
(
    day_month_year  integer     not null,
    week            varchar(2),
    hour            varchar(4),
    grid_number     varchar(10) not null,
    report_count    integer,
    life_population double precision,
    constraint congestion_pk
        primary key (day_month_year, grid_number)
);
