# Experiment 5: Greedy Best-First Search
import heapq

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [], "E": []
}
heuristic = {"A": 4, "B": 2, "C": 1, "D": 0, "E": 0}

def greedy_best_first(start, goal):
    queue = [(heuristic[start], start)]
    visited = set()
    while queue:
        _, node = heapq.heappop(queue)
        if node in visited:
            continue
        print(node, end=" ")
        visited.add(node)
        if node == goal:
            return
        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(queue, (heuristic[neighbour], neighbour))

greedy_best_first("A", "E")
