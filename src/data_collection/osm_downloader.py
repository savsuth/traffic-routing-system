import os
import osmnx as ox

PLACE_NAME = "Boston, Massachusetts, USA"
OUTPUT_DIR = "data/raw"
GRAPH_PATH = os.path.join(OUTPUT_DIR, "boston_drive.graphml")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Downloading road network for: {PLACE_NAME}")
    graph = ox.graph_from_place(PLACE_NAME, network_type="drive")

    print("Saving graph...")
    ox.save_graphml(graph, GRAPH_PATH)

    print("Download complete.")
    print(f"Nodes: {len(graph.nodes)}")
    print(f"Edges: {len(graph.edges)}")
    print(f"Saved to: {GRAPH_PATH}")


if __name__ == "__main__":
    main()
