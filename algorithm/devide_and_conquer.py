'''
分治算法（Divide and Conquer）是一种算法设计范式，
通过将问题分解为更小的子问题，递归地解决这些子问题，
然后合并它们的解来解决原问题。分治算法通常包括以下三个步骤：

分解（Divide）：将问题分解为若干个规模较小的子问题。
解决（Conquer）：递归地解决这些子问题。如果子问题足够小，则直接解决。
合并（Combine）：将子问题的解合并成原问题的解。
经典的分治算法包括归并排序（Merge Sort）、快速排序（Quick Sort）、二分查找（Binary Search）等。下面我们以归并排序为例，详细介绍分治算法的实现。

归并排序（Merge Sort）
归并排序是一种稳定的排序算法，采用分治策略，将数组分成两半，分别排序，然后合并两个有序数组。
时间复杂度为 O(n log n)。
空间复杂度：O(n)，用于存储临时数组。
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 分解
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合并
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # 合并两个有序数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # 处理剩余元素
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# 示例
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("排序后的数组:", sorted_arr)
