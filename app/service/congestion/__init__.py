# -*- coding: utf-8 -*-

def to_insert_list(df):
    return (df['day_month_year'],
            df['weekday'],
            df['hour'],
            df['tot_reg_cd'],
            df['report_count'],
            df['life_population'],
            df['name'])
