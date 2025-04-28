def tsp_nearest_neighbor(cities, distances):
    n = len(cities)
    visited = [False] * n
    visited[0] = True
    route = [cities[0]]
    current_city = 0

    for _ in range(n - 1):  
        nearest_city = None
        min_distance = float('inf')

        for i in range(n): 
            if not visited[i] and distances[current_city][i] < min_distance:
                min_distance = distances[current_city][i]
                nearest_city = i

        visited[nearest_city] = True
        route.append(cities[nearest_city])
        current_city = nearest_city

    route.append(cities[0])
    total_distance = 0
    for i in range(n):  
        from_city = cities.index(route[i]) 
        to_city = cities.index(route[i + 1])  
        total_distance += distances[from_city][to_city]

    return route, total_distance