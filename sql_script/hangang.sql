create table if not exists public.hangang
(
    year             integer,
    month            integer,
    day_month_year   integer    not null,
    weekday          varchar(2),
    grid_number      varchar(6) not null,
    ac_arrest        integer,
    ac_investigation integer,
    ac_end_report    integer,
    ac_not_handle    integer,
    ls_arrest        integer,
    ls_investigation integer,
    ls_end_report    integer,
    ls_not_handle    integer,
    ts_arrest        integer,
    ts_investigation integer,
    ts_end_report    integer,
    ts_not_handle    integer,
    md_arrest        integer,
    md_investigation integer,
    md_end_report    integer,
    md_not_handle    integer,
    name             varchar(30),
    constraint hangang_pk
        primary key (day_month_year, grid_number)
)

