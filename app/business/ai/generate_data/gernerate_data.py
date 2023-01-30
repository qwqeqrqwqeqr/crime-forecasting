from app.utils.constants import *


def generate_data(life_population,report,grid_map,grid_area_map):

    from app.business.ai.generate_data.life_population.concat_data import concat_grid_life_population, \
        calculate_life_population_average

    life_population = concat_grid_life_population(grid_area_map, calculate_life_population_average(
        life_population.life_population))

    from app.business.ai.generate_data.facility.concat_data import concat_grid_facility

    facility = concat_grid_facility(grid_map.grid_map, 2)  # 시설별 격자 데이터 산출

    dfs=[]

    from app.business.ai.generate_data import DF_LIST_SIZE
    for i in range(DF_LIST_SIZE):

        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        from app.business.ai.generate_data import evt_cl_cd_mask_list
        evt_cl_cd_mask = evt_cl_cd_mask_list(report.report)[i]

        report = count_point_in_polygon(grid_map.grid_map, '격자고유번호',
                                        report.report.loc[evt_cl_cd_mask],
                                        'x', 'y', EPSG_4326, False)

        df = [report, life_population] + facility

        from app.business.ai.generate_data.utils import grid_df_to_list, concat_grid_data
        dfs.append(concat_grid_data(grid_df_to_list(df), '격자고유번호'))

    return dfs