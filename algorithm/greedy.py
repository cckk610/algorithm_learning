'''
贪心算法（Greedy Algorithm）是一种在每一步选择中都采取当前状态下最好或最优（即最有利）的选择，
从而希望通过一系列局部最优选择达到全局最优的算法。贪心算法通常用于解决优化问题，如最小生成树、最短路径、活动选择等。
'''

'''
赫夫曼编码是一种用于数据压缩的贪心算法，通过构建赫夫曼树来生成最优前缀编码。
'''
import heapq
from collections import defaultdict

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if not data:
        return "", None

    # 计算字符频率
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    # 构建优先队列
    heap = [Node(freq=fr, char=ch) for ch, fr in freq.items()]
    heapq.heapify(heap)

    # 构建赫夫曼树
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    # 生成赫夫曼编码
    root = heap[0]
    huffman_code = {}

    def generate_code(node, current_code):
        if node is None:
            return
        if node.char is not None:
            huffman_code[node.char] = current_code
        generate_code(node.left, current_code + "0")
        generate_code(node.right, current_code + "1")

    generate_code(root, "")
    encoded_data = "".join(huffman_code[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return ""

    decoded_data = []
    node = root
    for bit in encoded_data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decoded_data.append(node.char)
            node = root

    return "".join(decoded_data)

# 示例
data = "this is an example for huffman encoding"
encoded_data, root = huffman_encoding(data)
print("编码后的数据:", encoded_data)
decoded_data = huffman_decoding(encoded_data, root)
print("解码后的数据:", decoded_data)

'''
1. 活动选择问题
活动选择问题是指在一组活动中选择尽可能多的互不重叠的活动。每个活动都有一个开始时间和结束时间，活动之间不能重叠。
'''
def activity_selection(activities):
    # 按结束时间排序
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    last_end_time = 0

    for activity in activities:
        if activity[0] >= last_end_time:
            selected_activities.append(activity)
            last_end_time = activity[1]

    return selected_activities

# 示例活动 (开始时间, 结束时间)
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
selected_activities = activity_selection(activities)
print("选择的活动:", selected_activities)

'''
分数背包问题是指在给定的物品中，每个物品都有重量和价值，要求在不超过背包容量的情况下，选择物品使得背包中的总价值最大。可以选择部分物品。
'''
def fractional_knapsack(capacity, items):
    # 按单位重量价值排序
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

# 示例物品 (重量, 价值)
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
max_value = fractional_knapsack(capacity, items)
print("最大价值:", max_value)
