import heapq

'''
Dijkstra算法是一种用于计算单源最短路径的经典算法，适用于加权有向图或无向图。
它的基本思想是通过贪心策略逐步扩展最短路径树，直到找到从源点到所有其他顶点的最短路径。

时间复杂度
时间复杂度：O((V+E)logV)，其中 
 V 是顶点数，
 E 是边数。使用优先队列（最小堆）可以有效地管理顶点的选择和距离更新。
空间复杂度：O(V+E)，用于存储图的邻接表和距离字典。
Dijkstra算法适用于加权图，但不适用于包含负权边的图。如果图中包含负权边，可以考虑使用Bellman-Ford算法。
'''

def dijkstra(graph, start):
    # 初始化距离字典，所有顶点的距离设置为无穷大
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # 起点的距离为0

    # 优先队列，存储 (距离, 顶点) 元组
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 如果当前距离大于已知的最短距离，则跳过
        if current_distance > distances[current_vertex]:
            continue

        # 遍历当前顶点的所有邻居
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # 如果找到更短的路径，则更新距离，并将邻居加入优先队列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 示例图的邻接表表示
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(f"从顶点 {start_vertex} 到其他顶点的最短距离: {distances}")
