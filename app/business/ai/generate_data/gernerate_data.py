from app.utils.constants import *

def generate_data(life_population,report,grid_map,grid_area_map):

    from app.business.ai.generate_data.life_population.concat_data import concat_grid_life_population,calculate_life_population_average
    life_population = concat_grid_life_population(grid_area_map, calculate_life_population_average(
        life_population.life_population))       # generate life population grid data

    from app.business.ai.generate_data.facility.concat_data import concat_grid_facility
    facility = concat_grid_facility(grid_map.grid_map, 2)       # generate facility grid data


    dfs=[]

    from app.business.ai import NAME_LIST_SIZE
    for i in range(NAME_LIST_SIZE):

        from app.business.preprocessing.count_point_in_polygon import count_point_in_polygon
        from app.business.ai import evt_cl_cd_mask_list
        evt_cl_cd_mask = evt_cl_cd_mask_list(report.report)[i]       # filter

        temp_report = count_point_in_polygon(grid_map.grid_map, '격자고유번호',
                                        report.report.loc[evt_cl_cd_mask],
                                        'x', 'y', EPSG_4326, False)       # generate report grid data

        temp_dfs = [temp_report, life_population] + facility       # concat all data

        from app.business.ai.utils import rename_dataframe, concat_grid_data
        from app.business.ai import GRID_NAME_LIST
        dfs.append(concat_grid_data(rename_dataframe(temp_dfs,'count',GRID_NAME_LIST), '격자고유번호'))

    return dfs