import unittest

from test.data_generator import *


class ValidatorTestSuite(unittest.TestCase):
    def test_validate_report_df_error(self):
        test = TEST_REPORT.rename(columns={'END_CD': 'FALSE_END_CD'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import validate_report_df
            validate_report_df(test)

    def test_validate_life_population_df_error(self):
        test = TEST_LIFE_POPULATION.rename(columns={'총생활인구수': 'FALSE_총생활인구수'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import validate_life_population_df
            validate_life_population_df(test)

    def test_validate_grid_df_error(self):
        test = TEST_GRID_MAP.rename(columns={'TOT_REG_CD': 'FALSE_TOT_REG_CD'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import validate_grid_df
            validate_grid_df(test)

    def test_validate_tourist_grid_df_error(self):
        test = TEST_GRID_TOURIST_MAP.rename(columns={'격자고유번호': 'FALSE_격자고유번호'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import tourist_grid_column_list
            tourist_grid_column_list(test)


    def test_validate_hangang_grid_df_error(self):
        test = TEST_GRID_HANGANG_MAP.rename(columns={'격자고유번호': 'FALSE_격자고유번호'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import hangang_grid_column_list
            hangang_grid_column_list(test)


    def test_validate_subway_grid_df_error(self):
        test = TEST_GRID_SUBWAY_MAP.rename(columns={'격자고유번호': 'FALSE_격자고유번호'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import subway_grid_column_list
            subway_grid_column_list(test)


    def test_validate_congestion_grid_df_error(self):
        test = TEST_GRID_AREA_MAP.rename(columns={'격자고유번호': 'FALSE_격자고유번호'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import validate_congestion_grid_df
            validate_congestion_grid_df(test)

    def test_validate_congestion_area_df_error(self):
        test = TEST_GRID_CONGESTION_MAP.rename(columns={'TOT_REG_CD': 'FALSE_TOT_REG_CD'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import validate_congestion_area_df
            validate_congestion_area_df(test)

    def test_validate_area_grid_df_error(self):
        test = TEST_AREA_CONGESTION_MAP.rename(columns={'격자고유번호': 'FALSE_격자고유번호'}, inplace=True)

        with self.assertRaises(Exception):
            from app.business.validator.validate_dataframe import validate_area_grid_df
            validate_area_grid_df(test)


if __name__ == '__main__':
    unittest.main()
