# -*- coding: utf-8 -*-


def service(life_population,report,grid_map,grid_area_map):

    from app.business.ai.generate_data.gernerate_data import generate_data
    generate_data_dfs = generate_data(life_population,report,grid_map,grid_area_map)
    save_train_data(generate_data_dfs[0])

    dfs= []
    from app.business.ai import NAME_LIST, NAME_LIST_SIZE
    for i in NAME_LIST_SIZE:
        from app.business.ai.train.train import train
        dfs.append(train(generate_data_dfs[i],NAME_LIST[i]))

    from app.business.ai.utils import concat_grid_data
    concat_data=concat_grid_data(dfs,'격자고유번호')
    

def save_train_data(train_data):
    from app.business.ai.generate_data import TRAIN_DATA_PATH
    train_data.to_csv(TRAIN_DATA_PATH)