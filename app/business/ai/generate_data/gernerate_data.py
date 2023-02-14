from app.utils.constants import *

EXPAND_DEPTH=2 # 2의 경우 8 방향 으로 2만큼 확장되기 때문에 총 500M가 됨 (1의 경우 300 2의 경우 500 3의 경우 700 ,...)
def generate_data(life_population,report_list,grid_map,grid_area_map):

    from app.business.ai.generate_data.life_population.concat_data import concat_grid_life_population,calculate_life_population_average
    life_population = concat_grid_life_population(grid_area_map, calculate_life_population_average(
        life_population.life_population))       # generate life population grid data

    from app.business.ai.generate_data.facility.concat_data import concat_grid_facility
    facility = concat_grid_facility(grid_map.grid_map, EXPAND_DEPTH)       # generate facility grid data


    dfs=[]

    for report in report_list:
        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        temp_report = count_point_in_polygon(grid_map.grid_map, '격자고유번호',
                                        report,
                                        'x', 'y', EPSG_4326, False)       # generate report grid data

        temp_dfs = [temp_report, life_population] + facility       # concat all data

        from app.business.ai.utils import rename_dataframe, concat_grid_data
        from app.business.ai.generate_data import GRID_NAME_LIST
        concat_df =concat_grid_data(rename_dataframe(temp_dfs,'count',GRID_NAME_LIST), '격자고유번호')
        dfs.append(concat_df)
    return dfs


