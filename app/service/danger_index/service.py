# -*- coding: utf-8 -*-

def service(life_population, report, grid_map, grid_area_map):
    from app.business.ai.generate_data.gernerate_data import generate_data
    generate_data_dfs = generate_data(life_population, report, grid_map, grid_area_map)
    save_train_data(generate_data_dfs)

    dfs = []
    from app.business.ai import NAME_LIST, NAME_LIST_SIZE
    for i in range(NAME_LIST_SIZE):         # loop by danger index
        from app.business.ai.train.train import train
        dfs.append(train(generate_data_dfs[i], NAME_LIST[i]))         # train generated data

    from app.business.ai.utils import concat_grid_data
    df = concat_grid_data(dfs, '격자고유번호')
    df['grid_number'] = df['격자고유번호'].map(lambda x: x[-6:])

    insert_data(df)



def save_train_data(train_data):        # save train data
    from app.business.ai import NAME_LIST_SIZE,NAME_LIST
    from app.business.ai.generate_data import TRAIN_DATA_PATH

    for i in range (NAME_LIST_SIZE):
        train_data.to_csv(TRAIN_DATA_PATH(NAME_LIST[i]))



def insert_data(df):  # insert in DB
    insert_list =[]
    for idx, row in df.iterrows():
        from app.service.danger_index import to_insert_list
        insert_list.append(to_insert_list(row))  # change format to insert in DB

    from app.database.query.danger_index import insert_danger
    insert_danger(insert_list)