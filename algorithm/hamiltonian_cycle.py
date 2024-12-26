'''
汉密尔顿回路（Hamiltonian Cycle）是图论中的一个经典问题，
指的是在一个图中找到一个回路，使得每个顶点恰好访问一次，并且最终回到起点。
这个问题是 NP 完全问题，因此没有已知的多项式时间算法来解决所有情况。

注意事项
该实现使用回溯法，适用于小规模图。对于大规模图，可能需要更高效的算法或启发式方法。
邻接矩阵表示法适用于稠密图，对于稀疏图，可以考虑使用邻接表表示法。

以下是使用回溯法（Backtracking）在 Python 中实现寻找汉密尔顿回路的示例代码：
'''

def is_safe(v, pos, path, graph):
    # 检查当前顶点是否与上一个顶点相连
    if graph[path[pos - 1]][v] == 0:
        return False

    # 检查当前顶点是否已经在路径中
    if v in path:
        return False

    return True

def hamiltonian_cycle_util(graph, path, pos):
    # 如果所有顶点都在路径中，并且最后一个顶点与第一个顶点相连
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # 尝试不同的顶点作为下一个候选顶点
    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v

            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True

            # 如果添加顶点 v 不成功，移除它
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  # 从第一个顶点开始

    if not hamiltonian_cycle_util(graph, path, 1):
        print("没有汉密尔顿回路")
        return False

    print("汉密尔顿回路存在: ", path + [path[0]])
    return True

# 示例图的邻接矩阵表示
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian_cycle(graph)
