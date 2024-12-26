'''
最小生成树（Minimum Spanning Tree, MST）是图论中的一个经典问题，
指的是在一个加权无向图中找到一棵树，使得这棵树包含图中的所有顶点，
并且边的权重之和最小。常用的算法有Kruskal算法和Prim算法。

Kruskal算法：O(ElogE+ElogV)，其中
 E 是边数，
 V 是顶点数。
排序边的时间复杂度为 O(ElogE)，
并查集操作的时间复杂度为 O(ElogV)。
'''

'''
Kruskal算法通过贪心策略，从小到大选择边，确保不会形成环，直到构建出最小生成树。
'''
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    edges = sorted(graph['edges'], key=lambda edge: edge[2])
    disjoint_set = DisjointSet(graph['vertices'])
    mst = []

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)

    return mst

# 示例图
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        ('A', 'B', 4),
        ('A', 'F', 2),
        ('B', 'C', 6),
        ('B', 'F', 5),
        ('C', 'D', 3),
        ('C', 'F', 1),
        ('D', 'E', 8),
        ('E', 'F', 7)
    ]
}

mst = kruskal(graph)
print("最小生成树的边:", mst)

'''
Prim算法从一个顶点开始，逐步扩展最小生成树，每次选择权重最小的边，直到包含所有顶点。

Prim算法： O(ElogV)，使用优先队列（最小堆）可以有效地管理顶点的选择和距离更新。
'''
import heapq

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (权重, 当前顶点, 前驱顶点)

    while min_heap:
        weight, current_vertex, prev_vertex = heapq.heappop(min_heap)
        if current_vertex not in visited:
            visited.add(current_vertex)
            if prev_vertex is not None:
                mst.append((prev_vertex, current_vertex, weight))

            for neighbor, edge_weight in graph[current_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return mst

# 示例图的邻接表表示
graph = {
    'A': {'B': 4, 'F': 2},
    'B': {'A': 4, 'C': 6, 'F': 5},
    'C': {'B': 6, 'D': 3, 'F': 1},
    'D': {'C': 3, 'E': 8},
    'E': {'D': 8, 'F': 7},
    'F': {'A': 2, 'B': 5, 'C': 1, 'E': 7}
}

start_vertex = 'A'
mst = prim(graph, start_vertex)
print("最小生成树的边:", mst)
