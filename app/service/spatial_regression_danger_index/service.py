def service(life_population, report, grid_map, grid_area_map):


    from app.business.ai.generate_data.gernerate_data import generate_data
    generate_data_dfs = generate_data(life_population, [report.report], grid_map,
                                      grid_area_map)  # generate concat predict data

    save_train_data(generate_data_dfs[0])
    from app.business.ai.danger_index.spatial_regression_danger_index import spatial_regression
    spatial_regression_result_df=spatial_regression(generate_data_dfs[0])

    save_result_data(spatial_regression_result_df)



def save_train_data(concat_df):        # save train data (전처리 후 데이터)
    from app.service.spatial_regression_danger_index import SR_DANGER_INDEX_TRAIN_DATA_PATH
    concat_df.to_csv(SR_DANGER_INDEX_TRAIN_DATA_PATH)

def save_result_data(concat_df):        # save result data (공간회귀 예측결과)
    from app.service.spatial_regression_danger_index import SR_DANGER_INDEX_RESULT_DATA_PATH
    concat_df.to_csv(SR_DANGER_INDEX_RESULT_DATA_PATH)