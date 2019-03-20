from django.test import TestCase
import datetime
from upload.views import read_xl_file
from upload.views import get_date

import openpyxl
import tempfile
import shutil
import pandas as pd
import os

# Create your tests here.


class read_xl_file_tests(TestCase):
    def test_empty_xls_xlsx_file(self):
        files = []
        wb = openpyxl.Workbook()
        wb.save('empty_xlsx_file.xlsx')
        files.append('empty_xlsx_file.xlsx')
        wb = openpyxl.Workbook()
        wb.save('empty_xls_file.xls')
        files.append('empty_xls_file.xls')
        for filename in files[0:2]:
            test_df = read_xl_file(filename)
            self.assertTrue(
                test_df[1] == "Заголовки таблицы не совпадают с контрольными")
            self.assertIsNone(test_df[0])
            os.remove(filename)

    def test_not_existing_file(self):
        filename = 'not_existing_file.xlsx'
        test_df = read_xl_file(filename)
        self.assertTrue(test_df[1] == "Файла не существует")
        self.assertIsNone(test_df[0])

    def test_not_xls_file(self):
        temp = open('not_excel_file.txt', 'w+b')
        temp.close()
        test_df = read_xl_file('not_excel_file.txt')
        self.assertTrue(test_df[1] == "Файл не является файлом .xls .xlsx")
        self.assertIsNone(test_df[0])
        os.remove('not_excel_file.txt')


class get_date_function_tests(TestCase):
    def test_date_test(self):
        input_string = "2019-11-01 23:15:50"
        test_date = get_date(input_string)
        self.assertEqual(test_date, "2019-11-01")

    # @skip("skip value error data test")
    # def test_date_test2(self):
    #     input_string = "2019/11/h01 23:15:50"
    #     test_date = get_date(input_string)
    #     self.assertEqual(test_date, "2019-11-01")


if __name__ == '__main__':
    unittest.main()
