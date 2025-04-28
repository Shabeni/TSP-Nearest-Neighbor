# Traveling Salesman Problem (TSP) - Nearest Neighbor Algorithm

A Python implementation of the **Nearest Neighbor Heuristic** for solving TSP.

## Usage
```python
cities = ['A', 'B', 'C']
distances = [
    [0, 10, 15],
    [10, 0, 20],
    [15, 20, 0]
]
route, distance = tsp_nearest_neighbor(cities, distances)
```

## Input Format
**cities**: List of city names (e.g., `['A', 'B', 'C']`)  
**distances**: 2D list where `distances[i][j]` = distance from `cities[i]` to `cities[j]`

## Time Complexity
**O(n²)** for n cities (due to nested loops)  
*Note*: The current implementation uses `list.index()` inside a loop, which could be optimized to O(n²) with a city-to-index dictionary
