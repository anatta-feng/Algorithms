states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()

while states_needed:
    best_station = None
    station_cover = set()
    for station, states in stations.items():
        cover = states_needed & states
        if len(cover) > len(station_cover):
            best_station = station
            station_cover = cover
    states_needed -= station_cover
    final_stations.add(best_station)

print(final_stations)
