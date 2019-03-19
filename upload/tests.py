from django.test import TestCase
from .views import read_xl_file
import openpyxl
import tempfile
import shutil
import pandas as pd
import os


# Create your tests here.


from unittest import TestCase


class read_xl_file_tests(TestCase):

    def ffff(self):
        self.fname = 'not_existing_file.xlsx'
        self.assertRaises(FileNotFoundError, read_xl_file, self.fname)
            

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
