def to_insert_list(df):
    return (df['day_month_year'],
            df['weekday'],
            df['hour'],
            df['grid_number'],
            df['report_count'],
            df['life_population'],
            df['name'])
