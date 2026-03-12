import heapq
import os
import sys
import osmnx as ox

sys.path.append(os.path.dirname(__file__))
from heuristics import haversine_distance

GRAPH_PATH = "data/raw/boston_drive.graphml"


def astar_search(graph, start, goal):
    open_heap = []
    heapq.heappush(open_heap, (0, start))

    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor in graph.neighbors(current):
            edge_data = graph.get_edge_data(current, neighbor)
            edge_length = min(d.get("length", 1.0) for d in edge_data.values())

            tentative_g = g_score[current] + edge_length

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                current_y = graph.nodes[neighbor]["y"]
                current_x = graph.nodes[neighbor]["x"]
                goal_y = graph.nodes[goal]["y"]
                goal_x = graph.nodes[goal]["x"]

                h = haversine_distance(current_y, current_x, goal_y, goal_x)
                f = tentative_g + h
                heapq.heappush(open_heap, (f, neighbor))

    return None, float("inf")


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def main():
    if not os.path.exists(GRAPH_PATH):
        print("Graph file not found. Run osm_downloader.py first.")
        return

    graph = ox.load_graphml(GRAPH_PATH)

    nodes = list(graph.nodes)
    start = nodes[0]
    goal = nodes[min(200, len(nodes) - 1)]

    path, cost = astar_search(graph, start, goal)

    if path is None:
        print("No path found.")
    else:
        print(f"Path found with {len(path)} nodes.")
        print(f"Approximate cost (meters): {cost:.2f}")


if __name__ == "__main__":
    main()
