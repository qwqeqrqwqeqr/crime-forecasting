from utils.utils import init

if __name__ == '__main__':

    #초기 검사
    init()

    # # 격자별 시설개수 구하기
    # from business.preprocessing.count_point_in_polygon.service import service as count_point_in_polygon
    # count_point_in_polygon()


    # 격자별 시설개수 합치기
    # 사전 격자별 시설개수 데이터들을 보유하고 있어야 함
    # from business.preprocessing.concat_grid_data.service import service as concat_grid_data
    # concat_grid_data()

    #  시설개수 확장하기
    #  사전 격자별 시설개수 데이터들을 보유하고 있어야 함
    # DEPTH = 2
    # from business.preprocessing.expand_data.service import service as  expand_data
    # expand_data(DEPTH,False)


    from business.preprocessing.calculate_life_population_avg.service import service as calculate_life_population_avg
    calculate_life_population_avg()

