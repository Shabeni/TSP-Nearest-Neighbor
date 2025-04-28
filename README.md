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
