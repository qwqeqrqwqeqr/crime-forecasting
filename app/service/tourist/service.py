import pandas as pd

from app.utils.constants import *

def service(area_map, grid_map, report):
    concat_df = pd.DataFrame()
    concat_df['grid_number'] = grid_map.grid_number

    from app.utils.codebook import end_cd_mask_list
    from app.service.tourist import name_list,evt_cl_cd_mask_list
    for i in range(len(name_list)):         # concat report data filtered evt_cd & evt_cl_cd
        concat_df = pd.merge(concat_df,
                             make_df(
                                 area_map, grid_map.grid_map,
                                 report.report,
                                 evt_cl_cd_mask_list(report.report)[i],     # 사건 종별 코드 마스킹
                                 end_cd_mask_list(report.report), name_list[i]),        # 종결 코드 마스킹
                             on='grid_number', how='inner')
    concat_df = concat_sub_data(report, concat_df)  # concat date df

    insert_data(concat_df)


def make_df(area_map, grid_map, report, evt_cl_cd_mask_list, end_cd_mask_list, name_list):      # 신고건수 필터링 후 관광지와 연결
    new_df = pd.DataFrame()
    for i in range(len(name_list)):
        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        count_point_df = count_point_in_polygon(grid_map, '격자고유번호',      # count report point in polygon
                                                report.loc[evt_cl_cd_mask_list & end_cd_mask_list[i]],
                                                'x', 'y', EPSG_4326, False)

        concat_df = pd.merge(area_map, count_point_df, on='격자고유번호', how='left')     # merge subway map
        new_df[name_list[i]] = concat_df['count']
        new_df['grid_number'] = concat_df['격자고유번호'].map(lambda x: x[-6:])
        new_df['name'] = concat_df['관광지']
    return new_df


def concat_sub_data(report, new_df):        # 부수적인 데이터 연결
    new_df.insert(0, 'weekday', str(report.weekday.iloc[0]))
    new_df.insert(0, 'day_month_year', str(report.day.iloc[0]))
    new_df.insert(0, 'month', str(report.day.iloc[0])[4:6])
    new_df.insert(0, 'year', str(report.day.iloc[0])[0:4])
    return new_df



def insert_data(df):        # insert in DB
    insert_list= []
    for idx, row in df.iterrows():
        from app.service.tourist import to_insert_list
        insert_list.append(to_insert_list(row))        # change format to insert in DB

    from app.database.query.tourist import insert_tourist
    insert_tourist(insert_list)
