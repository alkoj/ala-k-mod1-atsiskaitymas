import unittest
import os
import csv
import time
from ala_module.my_module_lit import crawl  # Импортируем функцию, если она будет реализована


class TestLrytas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Удаляем старый CSV файл перед выполнением тестов
        if os.path.exists("sorted_data.csv"):
            os.remove("sorted_data.csv")

    def test_file_creation(self):
        # Зададим лимит времени и вызовем функцию
        start_time = time.time()
        crawl(time_limit=60)  # Вызываем функцию crawl
        elapsed_time = time.time() - start_time

        # Проверяем, что файл создан
        self.assertTrue(os.path.exists("sorted_data.csv"), "Файл sorted_data.csv не был создан")

        # Проверяем, что файл содержит данные
        with open("sorted_data.csv", newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            # Убедимся, что в файле больше одной строки (чтобы учесть заголовок)
            self.assertGreater(len(rows), 1, "Файл sorted_data.csv не содержит данных")

    def test_time_limit(self):
        # Тестируем, что функция не превышает лимит времени
        start_time = time.time()
        crawl(time_limit=60)  # Вызываем функцию
        elapsed_time = time.time() - start_time

        # Проверяем, что функция выполнена за меньшее время, чем time_limit
        self.assertLess(elapsed_time, 60, "Функция выполнена дольше 60 секунд")


if __name__ == '__main__':
    unittest.main()