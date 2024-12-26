'''
拓扑排序（Topological Sorting）是对有向无环图（DAG）的一种线性排序，使得对于图中的每一条有向边
u→v
u→v，顶点u在排序中出现在顶点v之前。常用的拓扑排序算法有Kahn算法和深度优先搜索（DFS）算法。
'''

'''
Kahn算法基于入度的概念，通过不断移除入度为0的顶点来实现拓扑排序
O(V+E)，其中 
 V 是顶点数，
 E 是边数。
每个顶点和边都只会被处理一次。
'''
from collections import deque, defaultdict

def kahn_topological_sort(graph):
    in_degree = {u: 0 for u in graph}  # 初始化所有顶点的入度为0
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1  # 计算每个顶点的入度

    queue = deque([u for u in graph if in_degree[u] == 0])  # 入度为0的顶点入队
    topological_order = []

    while queue:
        u = queue.popleft()
        topological_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1  # 移除边 u -> v
            if in_degree[v] == 0:
                queue.append(v)  # 如果 v 的入度为0，则入队

    if len(topological_order) == len(graph):
        return topological_order
    else:
        raise ValueError("图中存在环，无法进行拓扑排序")

# 示例图的邻接表表示
graph = {
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': [],
    'G': []
}

topological_order = kahn_topological_sort(graph)
print("拓扑排序结果:", topological_order)



'''
DFS算法通过递归访问每个顶点，并在回溯时将顶点加入栈中，最终栈中的顶点顺序即为拓扑排序结果
O(V+E)，每个顶点和边都只会被访问一次。
'''
def dfs_topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]  # 逆序返回栈中的顶点

# 示例图的邻接表表示
graph = {
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': [],
    'G': []
}

topological_order = dfs_topological_sort(graph)
print("拓扑排序结果:", topological_order)
