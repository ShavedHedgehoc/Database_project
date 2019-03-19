from django.test import TestCase
from .views import read_xl_file
import tempfile, shutil
import os
from os import path





# Create your tests here.
class read_xl_file_tests(TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        # Установки запускаются перед каждым тестом
        

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        # Очистка после каждого метода
        

    # def test_file_not_exist(self):  # Пытаемся открыть несуществующий файл
    #     print("Checking not existing file...")
    #     testfile = "F:\notexisting.xls"
    #     test_df = read_xl_file(testfile)
    #     self.assertTrue(test_df[1] == "Файла не существует")
    #     self.assertTrue(test_df[0] is None)

    def test_empty_xls_file(self):  # Пытаемся открыть пустой файл xls
        filename = 'my_name.xls'
        temp = open(filename, 'w+b')
        temp.close()            
        test_df = read_xl_file(filename)
        print(filename)
        print(test_df[1])
        self.assertTrue(test_df[1] == "В файле нет данных, кроме заголовка")
        self.assertTrue(test_df[0] is None)
