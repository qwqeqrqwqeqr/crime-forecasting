from app.business.ai.train_data.life_population import \
    life_population_average
from app.utils.utils import init

'''
위험지수는 한 달 단위로 계산 됩니다.
122 신고 데이터 :  (현재 2021년 )
생활인구 데이터 포멧 :  (현재 : 2021년 데이터 총 365개)
PATH_GRID_AREA_MAP : 집계구 격자 데이터
PATH_GRID_MAP : 격자 데이터
'''

if __name__ == '__main__':
    # 초기 검사
    init()

    print("========== 위험지수를 산출 합니다. ==========")

    #생활인구 평균 계산
    calculate_life_population_average()

    #시설별 격자 데이터 산출
    from app.business.ai.train_data.facility.concat_data import report as get_facility_statistics
    get_facility_statistics(False,2)


    #  시설개수 확장하기
    #  사전 격자별 시설개수 데이터들을 보유하고 있어야 함
    # DEPTH = 2
    # from business.preprocessing.expand_data.report import report as expand_data
    #
    # expand_data(DEPTH, False)
