

def service(life_population,report, grid_map, grid_area_map,model,scaler):

        from app.business.ai.generate_data.gernerate_data import generate_data
        generate_data_dfs = generate_data(life_population, [report.report], grid_map,
                                          grid_area_map)  # generate concat predict data

        save_test_data(generate_data_dfs[0])       # list type 으로 받은 이유는 다른 예측 코드와 통일성 맞추기 위함
        from app.business.ai.predict.test import test as predict
        predict_result_df=predict(generate_data_dfs[0],model,scaler)        # 테스트 진행
        predict_result_df(save_result_data)


def save_test_data(concat_df):        # save test data (전처리 후 데이터)
    from app.service.predict.test import PREDICT_TEST_DATA_PATH
    concat_df.to_csv(PREDICT_TEST_DATA_PATH)

def save_result_data(concat_df):        # save result data (예측결과)
    from app.service.predict.test import PREDICT_RESULT_DATA_PATH
    concat_df.to_csv(PREDICT_RESULT_DATA_PATH)