# -*- coding: utf-8 -*-

import pandas as pd


from app.utils.constants import *

'''
Run Parameters
- REPORT_PATH: report directory path (ex) "./test/data/report/"
- LIFE_POPULATION_PATH: life population directory path (ex) "./test/data/life_population/"

PATH_GRID_MAP : 100 grid data 
PATH_GRID_AREA_MAP : area(집계구) grid data

실행 방식
1. 훈련과 테스트 동시 진행(base) : model scaler 및 예측 결과가 산출됨 (파일로 저장)
    - 모든 데이터를 전부 주입함
    - REPORT_PATH,TRAIN_LIFE_POPULATION_PATH,PREDICT_POPULATION_PATH,MODEL,SCALER
2. 훈련 만 진행 : model 과 scaler 가 산출됨 
    - 112 신고데이터와 훈련용 생활 인구 만 주입 나머지는 None 으로 입력
    - REPORT_PATH,TRAIN_LIFE_POPULATION_PATH,None,None,None
3. 테스트 만 진행(이미 model 과 scaler 를 보유 하고 있을 시 사용 가능)  : 예측결과가 산출됨
    - 112 신고데이터와 훈련용 생활 인구 만 주입 나머지는 None 으로 입력
    - REPORT_PATH,TRAIN_LIFE_POPULATION_PATH,None,None,None
'''
