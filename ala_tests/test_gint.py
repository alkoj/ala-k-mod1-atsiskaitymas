import unittest
import os
import csv
import time
from ala_module.my_module_gint import scrape_products  # Importuokite reikalingą funkciją


class TestScraper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Pasenusių CSV failų pašalinimas prieš testų vykdymą
        if os.path.exists("products.csv"):
            os.remove("products.csv")

    def test_time_limit(self):
        start_time = time.time()
        scrape_products(time_limit=20)  # Nustatykite laiko limitą
        elapsed_time = time.time() - start_time

        # Patikriname, ar praėjo mažiau nei 20 sekundžių
        self.assertLess(elapsed_time, 20, "Žvalgymas užtruko daugiau nei 20 sekundžių")

    def test_csv_output(self):
        scrape_products(time_limit=20)  # Iškvieskite funkciją, kad sukurtumėte CSV

        # Patikriname, ar failas sukurtas
        self.assertTrue(os.path.exists("products.csv"), "Failas products.csv nebuvo sukurtas")

        # Patikriname, ar faile yra duomenų
        with open("products.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertGreater(len(rows), 1, "Failas products.csv neturi duomenų")


if __name__ == '__main__':
    unittest.main()