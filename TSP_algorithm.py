import itertools

def calculate_total_distance(path,distances):
    total_distance=0
    num_cities=len(path)

    for i in range(num_cities-1):
        total_distance += distances[path[i]][path[i+1]]
    total_distance += distances[path[-1]][path[0]]
    return total_distance


def find_shortest_path(cities,distances):
    shortest_distance=float('inf')
    shortest_path=None
    num_cities=len(cities)

    all_paths= itertools.permutations(range(num_cities))

    for path in all_paths:
        distance=calculate_total_distance(path,distances)
        if distance < shortest_distance:
            shortest_distance=distance
            shortest_path=path

    return shortest_path,shortest_distance

cities=['A','B','C','D']

distances=[
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_path, shortest_distance = find_shortest_path(cities, distances)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)