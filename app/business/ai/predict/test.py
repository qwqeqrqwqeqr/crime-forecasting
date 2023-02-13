from app.business.ai.predict import *


def test(train_data_df,model,scaler):
    train_data_df = generate_filter_class(train_data_df)  # generate filter class
    x, y = generate_xy_class(train_data_df)  # generate data for predict model
    x = generate_test_data(x,scaler)
    predict_model = model.predict(x)

    report_model(model,predict_model,x,y)
    return generate_predict_df(train_data_df,model,x,y)


def report_model(model,predict_model, x_test, y_test):      # model에 대한 보고서 출력
    from log import logger
    from sklearn.metrics import classification_report
    logger.info(f"%s" %classification_report(y_test, predict_model))
    from sklearn.metrics import roc_auc_score
    logger.info(f"roc_auc_score : %s" %roc_auc_score(y_test, model.predict_proba(x_test), multi_class='ovr'))

def generate_predict_df(train_data_df,model, x_test, y_test):     #  예측된 데이터 추출
    predict_df = train_data_df.iloc[:, :-1]
    predict_df['실제클래스'] = y_test
    predict_df['예측클래스'] = model.predict(x_test)
    predict_df[['pred_proba=0', 'pred_proba=1', 'pred_proba=2']] = model.predict_proba(x_test).tolist()
    return predict_df
def generate_test_data(x,scaler):
    x_test = x.iloc[:, 2:]
    import pandas as pd
    return pd.DataFrame(scaler.transform(x_test), columns=x_test.columns)



