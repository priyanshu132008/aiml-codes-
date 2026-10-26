# Experiment 6: A* Search
import heapq

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 2, "E": 5},
    "C": {"E": 1},
    "D": {"E": 1},
    "E": {}
}
h = {"A": 4, "B": 3, "C": 1, "D": 1, "E": 0}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    best_cost = {start: 0}
    while queue:
        _, cost, node, path = heapq.heappop(queue)
        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", cost)
            return
        for neighbour, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                heapq.heappush(queue, (new_cost + h[neighbour],
                                       new_cost, neighbour, path + [neighbour]))

astar("A", "E")
