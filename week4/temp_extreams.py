import sys
import os
import csv


def find_station_id_by_name(station, file):
    if station == "":
        raise ValueError("station name is empty")
    if file == "":
        raise ValueError("stations file name is empty")
    if not os.path.exists(file):
        raise ValueError('file %s  does not exist' % file)
    ret = None
    with open(file, "rt") as f:
        for line in f:
            station_id = line[0:11]
            nm = line[41:70].strip()
            if nm == station:
                ret = station_id

    return ret


def find_max_and_min_temp_by_id(station_id, file):
        if station_id == "":
            raise ValueError("station id is empty")
        if file == "":
            raise ValueError("data file name is empty")
        if not os.path.exists(file):
            raise ValueError('file %s  does not exist' % file)
        max_temp = []
        min_temp = []
        with open(file) as f:
            f_csv = csv.reader(f)
            for row in f_csv:

                if row[0] == station_id and row[2].startswith("TMAX") and row[3] != "":
                    max_v = round(int(row[3])*0.1, 1)
                    max_v_l = [row[1], max_v]
                    max_temp.append(max_v_l)
                if row[0] == station_id and row[2].startswith("TMIN") and row[3] != "":
                    min_v = round(int(row[3])*0.1, 1)
                    min_v_l = [row[1], min_v]
                    min_temp.append(min_v_l)
        if not max_temp or not min_temp:
            return None
        mx = max(max_temp, key=lambda x: x[1])
        mn = min(min_temp, key=lambda x: x[1])
        result = [mx, mn]
        return result


def main():

    if len(sys.argv) != 2:
        print('usage: ./tempextreams.py <station name>')
        sys.exit(1)
    else:
        station_name = sys.argv[1]
        stations_file_path = "c:/temp/week4/ghcnd-stations.txt"
        station_id = find_station_id_by_name(station_name, stations_file_path)
        data_file_path = "c:/temp/week4/2017.csv"
        if station_id is None:
            print("cannot find station with the name=%s" % station_name)
            sys.exit(1)
        else:
            data = find_max_and_min_temp_by_id(station_id, data_file_path)
            if data is not None:
                print("Max Temperature %s observed on %s" % (data[0][1], data[0][0]))
                print("Min Temperature %s observed on %s" % (data[1][1], data[1][0]))


if __name__ == '__main__':
    main()
