

def service(report, grid_map, grid_area_map, life_population,model,scaler):

        from app.business.ai.generate_data.gernerate_data import generate_data
        generate_data_dfs = generate_data(life_population, [report.report], grid_map,
                                          grid_area_map)  # generate concat predict data

        save_test_data(generate_data_dfs[0])
        from app.business.ai.predict.test import test as predict
        predict_result_df=predict(generate_data_dfs[0],model,scaler)
        predict_result_df(save_result_data)


def save_test_data(concat_df):        # save test data (전처리 후 데이터)
    from app.service.predict.test import PREDICT_TEST_DATA_PATH
    concat_df.to_csv(PREDICT_TEST_DATA_PATH)

def save_result_data(concat_df):        # save result data (예측결과)
    from app.service.predict.test import PREDICT_RESULT_DATA_PATH
    concat_df.to_csv(PREDICT_RESULT_DATA_PATH)