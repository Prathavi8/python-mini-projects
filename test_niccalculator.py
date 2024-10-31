import unittest
import niccalculator

class testniccalculator (unittest.TestCase):

    def test_born_date_for_male(self):
        nic = "197900209871"
        born_date = niccalculator.get_born_date(nic)
        born_year = born_date.year
        born_month = born_date.month
        born_day = born_date.day

        self.assertEqual(born_year, 1979)
        self.assertEqual(born_month, 1)
        self.assertEqual(born_day, 2)

    def test_born_date_for_female(self):
        nic = "197900209871"
        born_date = niccalculator.get_born_date(nic)
        born_year = born_date.year
        born_month = born_date.month
        born_day = born_date.day

        self.assertEqual(born_year, 1979)
        self.assertEqual(born_month, 1)
        self.assertEqual(born_day, 2)


if __name__ == '__main__':
    unittest.main()