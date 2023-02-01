from pandas import DataFrame

report_column_list = ['RECV_NO', 'DAY', 'TIME', 'EVT_CL_CD', 'RECV_EMG_CD', 'RPTER_SEX',
                      'TRC_TYPE', 'HPPN_Y_SW', 'HPPN_X_SW', 'HPPN_Y_NE', 'HPPN_X_NE',
                      'HPPN_Y_NW', 'HPPN_X_NW', 'HPPN_Y_SE', 'HPPN_X_SE', 'END_CD']

life_population_column_list = ['?"기준일ID"', '시간대구분', '행정동코드', '집계구코드', '총생활인구수', '남자0세부터9세생활인구수',
                               '남자10세부터14세생활인구수', '남자15세부터19세생활인구수', '남자20세부터24세생활인구수', '남자25세부터29세생활인구수',
                               '남자30세부터34세생활인구수', '남자35세부터39세생활인구수', '남자40세부터44세생활인구수', '남자45세부터49세생활인구수',
                               '남자50세부터54세생활인구수', '남자55세부터59세생활인구수', '남자60세부터64세생활인구수', '남자65세부터69세생활인구수',
                               '남자70세이상생활인구수', '여자0세부터9세생활인구수', '여자10세부터14세생활인구수', '여자15세부터19세생활인구수',
                               '여자20세부터24세생활인구수', '여자25세부터29세생활인구수', '여자30세부터34세생활인구수', '여자35세부터39세생활인구수',
                               '여자40세부터44세생활인구수', '여자45세부터49세생활인구수', '여자50세부터54세생활인구수', '여자55세부터59세생활인구수',
                               '여자60세부터64세생활인구수', '여자65세부터69세생활인구수', '여자70세이상생활인구수']

grid_column_list = ['격자고유번호', '남자0~4세', '남자5~9세', '남자10~14세', '남자15~19세', '남자20~24세', '남자25~29세',
                    '남자30~34세', '남자35~39세', '남자40~44세', '남자45~49세', '남자50~54세', '남자55~59세',
                    '남자60~64세', '남자65~69세', '남자70~74세', '남자75~79세', '남자80~84세', '남자85~89세',
                    '여자0~4세', '여자5~9세', '여자10~14세', '여자15~19세', '여자20~24세', '여자25~29세', '여자30~34세',
                    '여자35~39세', '여자40~44세', '여자45~49세', '여자50~54세', '여자55~59세', '여자60~64세',
                    '여자65~69세', '여자70~74세', '여자75~79세', '여자80~84세', '여자85~89세', 'geometry']


tourist_grid_column_list = ['격자고유번호', '관광지']
subway_grid_column_list=['격자고유번호', '지하철']
hangang_grid_column_list=['격자고유번호', '한강']
congestion_grid_column_list=['격자고유번호', 'category', '혼잡지역']
area_grid_column_list=['격자고유번호', 'TOT_REG_CD', 'ADM_NM', 'ADM_CD', 'duplicate']

def validate_report_df(report: DataFrame):
    if False in (report.columns.values == report_column_list):
        from log import logger
        logger.info("[Error] [Report] Incorrect file format")
        raise EnvironmentError


def validate_life_population_df(life_population: DataFrame):
    if False in (life_population.columns.values == life_population_column_list):
        from log import logger
        logger.info("[Error] [Life Population] Incorrect file format")
        raise EnvironmentError


def validate_grid_df(grid: DataFrame):
    if False in (grid.columns.values == grid_column_list):
        from log import logger
        logger.info("[Error] [Grid] Incorrect file format")
        raise EnvironmentError


def validate_tourist_grid_df(grid: DataFrame):
    if False in (grid.columns.values == tourist_grid_column_list):
        from log import logger
        logger.info("[Error] [Tourist Grid] Incorrect file format")
        raise EnvironmentError

def validate_hangang_grid_df(grid: DataFrame):
    if False in (grid.columns.values == hangang_grid_column_list):
        from log import logger
        logger.info("[Error] [Hangang Grid] Incorrect file format")
        raise EnvironmentError


def validate_subway_grid_df(grid: DataFrame):
    if False in (grid.columns.values == subway_grid_column_list):
        from log import logger
        logger.info("[Error] [Subway Grid] Incorrect file format")
        raise EnvironmentError


def validate_congestion_grid_df(grid: DataFrame):
    if False in (grid.columns.values == congestion_grid_column_list):
        from log import logger
        logger.info("[Error] [Congestion Grid] Incorrect file format")
        raise EnvironmentError

def validate_area_grid_df(grid: DataFrame):
    if False in (grid.columns.values == congestion_grid_column_list):
        from log import logger
        logger.info("[Error] [Area Grid] Incorrect file format")
        raise EnvironmentError