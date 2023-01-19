create table if not exists public.danger_index
(
    grid_number     varchar(6) not null
        constraint danger_index_pk
            primary key,
    dv_danger_index double precision,
    tp_danger_index double precision,
    sh_danger_index double precision,
    da_danger_index double precision,
    st_danger_index double precision,
    ca_danger_index double precision,
    sv_danger_index double precision
)


