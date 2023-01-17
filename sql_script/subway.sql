create table if not exists public.subway
(
    year             integer,
    month            integer,
    day_month_year   integer     not null,
    weekday          varchar(2),
    grid_number      varchar(10) not null,
    ac_arrest        integer,
    ac_investigation integer,
    ac_end_report    integer,
    ac_not_handle    integer,
    pp_arrest        integer,
    pp_investigation integer,
    pp_end_report    integer,
    pp_not_handle    integer,
    gc_arrest        integer,
    gc_investigation integer,
    gc_end_report    integer,
    gc_not_handle    integer,
    cr_arrest        integer,
    cr_investigation integer,
    cr_end_report    integer,
    cr_not_handle    integer,
    md_arrest        integer,
    md_investigation integer,
    md_end_report    integer,
    md_not_handle    integer,
    constraint subway_pk
        primary key (day_month_year, grid_number)
);

