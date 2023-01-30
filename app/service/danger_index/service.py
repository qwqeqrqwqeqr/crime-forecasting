# -*- coding: utf-8 -*-


def service(life_population,report,grid_map,grid_area_map):

    from app.business.ai.generate_data.gernerate_data import generate_data
    dfs = generate_data(life_population,report,grid_map,grid_area_map)

    print(dfs)
    # save_train_data(dfs[0])
    #
    #
    #
    # from app.business.ai.train.train import train
    # df = train(dfs[0],"dv_danger_index")
    #
    # print(df)


def save_train_data(train_data):
    from app.business.ai.generate_data import TRAIN_DATA_PATH
    train_data.to_csv(TRAIN_DATA_PATH)