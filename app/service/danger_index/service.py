# -*- coding: utf-8 -*-


def service(life_population, report, grid_map, grid_area_map):

    report_list = []        # generate mask filtered report list
    from app.service.danger_index import evt_cl_cd_mask_list
    for i in range(len(evt_cl_cd_mask_list(report.report))):        # get filtered report df
        report_list.append(report.report.loc[evt_cl_cd_mask_list(report.report)[i]])

    from app.business.ai.generate_data.gernerate_data import generate_data
    generate_data_dfs = generate_data(life_population, report_list, grid_map, grid_area_map)        # generate concat predict data

    dfs = []
    from app.service.danger_index import DANGER_INDEX_NAME_LIST
    for i in range(len(DANGER_INDEX_NAME_LIST)):         # loop by danger index

        save_data(generate_data_dfs[i],DANGER_INDEX_NAME_LIST[i])
        from app.business.ai.danger_index.danger_index import generate_danger_index
        dfs.append(generate_danger_index(generate_data_dfs[i], DANGER_INDEX_NAME_LIST[i]))         # predict

    from app.business.ai.utils import concat_grid_data
    df = concat_grid_data(dfs, '격자고유번호')
    df['grid_number'] = df['격자고유번호'].map(lambda x: x[-6:])

    insert_data(df)

def save_data(concat_df,key_danger_index):        # save predict data
    from app.service.danger_index import DANGER_INDEX_DATA_PATH
    concat_df.to_csv(DANGER_INDEX_DATA_PATH(key_danger_index))


def insert_data(df):  # insert in DB
    insert_list =[]
    for idx, row in df.iterrows():
        from app.service.danger_index import to_insert_list
        insert_list.append(to_insert_list(row))  # change format to insert in DB

    from app.database.query.danger_index import insert_danger
    insert_danger(insert_list)