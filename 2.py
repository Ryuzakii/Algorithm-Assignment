class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.edges = []  # List to store graph edges (u, v, weight)

    def add_edge(self, u, v, weight):
        """
        Add an edge to the graph.
        """
        self.edges.append((u, v, weight))

    def find(self, parent, i):
        """
        Find the root of the set containing element i with path compression.
        """
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    def union(self, parent, rank, x, y):
        """
        Union of two sets using union by rank.
        """
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if root_x != root_y:
            # Attach smaller rank tree under root of higher rank tree
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def kruskal_mst(self):
        """
        Kruskal's algorithm to find the MST of the graph.
        Returns the total weight and the edges in the MST.
        """
        # Step 1: Sort all edges by weight
        self.edges.sort(key=lambda x: x[2])

        parent = []  # Parent array for Union-Find
        rank = []  # Rank array for Union-Find

        # Initialize Union-Find structures
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        mst = []  # Store edges in the MST
        mst_weight = 0  # Total weight of the MST

        # Step 2: Pick edges one by one
        for u, v, weight in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # If including this edge does not cause a cycle
            if root_u != root_v:
                mst.append((u, v, weight))
                mst_weight += weight
                self.union(parent, rank, root_u, root_v)

            # Stop if MST has V-1 edges
            if len(mst) == self.vertices - 1:
                break

        return mst_weight, mst


# Test the implementation
if __name__ == "__main__":
    # Create a graph with 4 vertices
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    # Find the MST
    mst_weight, mst_edges = g.kruskal_mst()

    print("Edges in the MST:")
    for u, v, weight in mst_edges:
        print(f"({u}, {v}) - Weight: {weight}")

    print(f"\nTotal weight of the MST: {mst_weight}")
