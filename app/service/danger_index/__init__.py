def to_insert_list(df):
    return (
    df['grid_number'], df['dv_danger_index'], df['tp_danger_index'],
    df['sh_danger_index'], df['da_danger_index'],
    df['st_danger_index'], df['ca_danger_index'], df['sv_danger_index'])
