from utils.utils import init

if __name__ == '__main__':

    DEPTH =2

    init()

    # 격자별 시설개수 구하기
    from business.preprocessing.count_point_in_polygon.service import service as count_point_in_polygon
    count_point_in_polygon()

    # 시설개수 확장하기
    from business.preprocessing.expand_data.service import service as  expand_data
    expand_data(DEPTH,False)


