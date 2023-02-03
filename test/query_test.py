import unittest

from test.data_generator import *


class ValidatorTestSuite(unittest.TestCase):

    # def test_insert_report(self):
    #     from app.database.query.report import insert_report, select_all_report
    #     insert_report(REPORT_DATA_SAMPLE)
    #     self.assertEqual(len(select_all_report()),1)



    def test_insert_subway(self):
        from app.database.query.subway import insert_subway, select_all_subway
        insert_subway(SUBWAY_DATA_SAMPLE)
        print(select_all_subway())
        self.assertEqual(len(select_all_subway()),1)

