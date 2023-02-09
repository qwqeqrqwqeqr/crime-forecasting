

def service(report, grid_map, grid_area_map,train_life_population, predict_life_population,model,scaler):

    train_scaler = scaler
    train_model = model

    if train_life_population is not None:       # train

        from app.business.ai.generate_data.gernerate_data import generate_data
        generate_data_dfs = generate_data(train_life_population, [report.report], grid_map,
                                          grid_area_map)  # generate concat predict data

        save_train_data(generate_data_dfs[0])       # list type 으로 받은 이유는 다른 예측 코드와 통일성 맞추기 위함

        from app.business.ai.predict.train import train
        temp_model,temp_scaler=train(generate_data_dfs[0])        # train model
        train_scaler = temp_scaler
        train_model = temp_model

    if predict_life_population is not None:

        from app.business.ai.generate_data.gernerate_data import generate_data
        generate_data_dfs = generate_data(predict_life_population, [report.report], grid_map,
                                          grid_area_map)  # generate concat predict data

        save_test_data(generate_data_dfs[0])
        from app.business.ai.predict.predict import predict
        predict_result_df=predict(generate_data_dfs[0],train_model,train_scaler)
        predict_result_df(save_result_data)

def save_train_data(concat_df):        # save train data (전처리 후 데이터)
    from app.service.predict import PREDICT_TRAIN_DATA_PATH
    concat_df.to_csv(PREDICT_TRAIN_DATA_PATH)

def save_test_data(concat_df):        # save test data (전처리 후 데이터)
    from app.service.predict import PREDICT_TEST_DATA_PATH
    concat_df.to_csv(PREDICT_TEST_DATA_PATH)

def save_result_data(concat_df):        # save result data (예측결과)
    from app.service.predict import PREDICT_RESULT_DATA_PATH
    concat_df.to_csv(PREDICT_RESULT_DATA_PATH)