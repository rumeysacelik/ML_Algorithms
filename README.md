# TSP and KNN Algorithms

This repository contains implementations of the Travelling Salesman Problem (TSP) algorithm and the K-Nearest Neighbors (KNN) algorithm in Python.

## TSP_algorithm.py

This script provides a solution to the Travelling Salesman Problem using a brute-force approach to find the shortest possible route that visits each city and returns to the origin city.

### Features

- Calculate the total distance for a given path.
- Find the shortest path by examining all permutations of city visits.

### Usage

1. Define the list of cities.
2. Define the distance matrix representing distances between each pair of cities.
3. Run the script to find and print the shortest path and its distance.

#### Example

```python
cities = ['A', 'B', 'C', 'D']

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_path, shortest_distance = find_shortest_path(cities, distances)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)
