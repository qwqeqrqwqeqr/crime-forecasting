create table if not exists digitalif.congestion
(
    day_month_year  integer    not null,
    weekday         varchar(2),
    hour            varchar(4) not null,
    tot_reg_code     varchar(13) not null,
    report_count    integer,
    life_population double precision,
    name            varchar(30),
    constraint congestion_pk
        primary key (day_month_year, tot_reg_code, hour)
)

