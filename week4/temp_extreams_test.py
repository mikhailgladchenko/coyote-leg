import unittest
from week4.temp_extreams import find_station_id_by_name
from week4.temp_extreams import find_max_and_min_temp_by_id


class TestFiles(unittest.TestCase):

    def test_exception1(self):
        with self.assertRaises(ValueError):
            station_file_name = "c:/temp/week4/ghcnd-stations.txt"
            find_station_id_by_name("", station_file_name)

    def test_exception2(self):
        with self.assertRaises(ValueError):
            station = "VILNIUS"
            find_station_id_by_name(station, "")

    def test_exception3(self):
        with self.assertRaises(ValueError):
            station = "VILNIUS"
            station_file_name = "c:/temp/unknown.txt"
            find_station_id_by_name(station, station_file_name)

    def test_value1(self):
        station = "VILNIUS"
        station_file_name = "c:/temp/week4/ghcnd-stations.txt"
        self.assertEqual(find_station_id_by_name(station, station_file_name), "LH000026730")

    def test_value2(self):
        station = "HERAT"
        station_file_name = "c:/temp/week4/ghcnd-stations.txt"
        self.assertEqual(find_station_id_by_name(station, station_file_name), "AFM00040938")

    def test_value3(self):
        station = "YAROSLAVL"
        station_file_name = "c:/temp/week4/ghcnd-stations.txt"
        self.assertEqual(find_station_id_by_name(station, station_file_name), None)

    def test_exception4(self):
        with self.assertRaises(ValueError):
            data_file_name = "c:/temp/week4/2017.csv"
            find_max_and_min_temp_by_id("", data_file_name)

    def test_exception5(self):
        with self.assertRaises(ValueError):
            find_max_and_min_temp_by_id("LH00002673", "")

    def test_exception6(self):
        with self.assertRaises(ValueError):

            find_max_and_min_temp_by_id("LH00002673", "c:/temp/week4/unknown.csv")

    def test_value4(self):
        station_id = "Unknown"
        data_file_name = "c:/temp/week4/2017.csv"
        self.assertEqual(find_max_and_min_temp_by_id(station_id, data_file_name), None)

    def test_value5(self):
        station_id = "LH000026730"
        data_file_name = "c:/temp/week4/2017.csv"
        self.assertEqual(find_max_and_min_temp_by_id(station_id, data_file_name)[0][1], 28.6)

    def test_value6(self):
        station_id = "LH000026730"
        data_file_name = "c:/temp/week4/2017.csv"
        self.assertEqual(find_max_and_min_temp_by_id(station_id, data_file_name)[1][1], -23.5)


if __name__ == '__main__':
    unittest.main()
