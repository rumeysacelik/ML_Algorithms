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
]```


shortest_path, shortest_distance = find_shortest_path(cities, distances)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)


# KNN_algorithm.py

This script implements the K-Nearest Neighbors algorithm for classification. It predicts the class of a given test sample based on the majority class among its `k` nearest neighbors in the training dataset.

## Features

- Initialize the KNN model with a specified `k` value.
- Fit the model with training data.
- Predict the class labels for test data.

## Usage

1. Define the training data (`X_train`) and corresponding labels (`y_train`).
2. Define the test data (`X_test`).
3. Initialize the KNN model and fit it with the training data.
4. Predict the labels for the test data and print the predictions.

### Example

```python
import numpy as np
from knn_algorithm import KNN

X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([0, 0, 1, 1])
X_test = np.array([[2.5, 3.5]])

model = KNN(k=3)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Predictions:", predictions)

