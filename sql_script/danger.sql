create table if not exists public.danger
(
    grid_number     varchar(10) not null
        constraint danger_pk
            primary key,
    hc_danger_index double precision,
    gc_danger_index double precision,
    cc_danger_index double precision
);

