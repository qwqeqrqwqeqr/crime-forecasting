from app.database.query.congestion import get_all_congestion
from app.utils.utils import init

if __name__ == '__main__':
    # 초기 검사
    init()
    get_all_congestion()


    #시설별 격자 데이터 산출
    # from app.business.statistics.facility_statistics.service import service as get_facility_statistics
    # get_facility_statistics(False,2)

    # 혼잡도 산출
    # from business.statistics.congestion_statistics.service import service as get_congestion_statistics
    # get_congestion_statistics()

    #  시설개수 확장하기
    #  사전 격자별 시설개수 데이터들을 보유하고 있어야 함
    # DEPTH = 2
    # from business.preprocessing.expand_data.service import service as expand_data
    #
    # expand_data(DEPTH, False)
