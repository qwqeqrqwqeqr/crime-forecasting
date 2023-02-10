def service(life_population,report, grid_map, grid_area_map):
    from app.business.ai.generate_data.gernerate_data import generate_data
    generate_data_dfs = generate_data(life_population, [report.report], grid_map,
                                      grid_area_map)  # generate concat predict data

    save_train_data(generate_data_dfs[0])  # list type 으로 받은 이유는 다른 예측 코드와 통일성 맞추기 위함

    from app.business.ai.predict.train import train
    train(generate_data_dfs[0])  # train model


def save_train_data(concat_df):  # save train data (전처리 후 데이터)
    from app.service.predict.train import PREDICT_TRAIN_DATA_PATH
    concat_df.to_csv(PREDICT_TRAIN_DATA_PATH)
