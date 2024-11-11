# Write your solution here

import math

def get_station_data(filename: str):
    location = ()
    station_dict = {}
    with open(filename) as stations:
        for station in stations:
            station = station.replace("\n", "")
            station = station.split(";")
            if station[0] == "Longitude":
                continue
            location = float(station[0]),  float(station[1])
            station_dict[station[3]] = location
    return station_dict

def distance(stations: dict, station1: str, station2: str):
    long1, lat1 = stations[station1]
    long2, lat2 = stations[station2]
    x = (long1 - long2) * 55.26
    y = (lat1 - lat2) * 111.2
    distance = math.sqrt(x**2 + y**2)
    return distance

def greatest_distance(stations: dict):
    distance_value = 0
    for station1 in stations:
        for station2 in stations:
            if distance(stations, station1, station2) > distance_value:
                distance_value = distance(stations, station1, station2)
                greatest_station1 = station1
                greatest_station2 = station2
    return (greatest_station1, greatest_station2, distance_value)

if __name__ == "__main__":  
    station_dict = get_station_data("stations1.csv")
    print(distance(station_dict, "Kaivopuisto", "Laivasillankatu"))
    print(greatest_distance(station_dict))