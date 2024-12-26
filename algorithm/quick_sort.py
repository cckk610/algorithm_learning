'''
快速排序（QuickSort）是一种高效的排序算法，采用分治法（Divide and Conquer）策略。
它的基本思想是选择一个“基准”元素，通过一趟排序将待排序序列分成两部分，
其中一部分的所有元素都比基准元素小，另一部分的所有元素都比基准元素大，然后递归地对这两部分进行排序。


时间复杂度
平均时间复杂度：O(nlogn)，其中 n 是数组的长度。
最坏时间复杂度：O(n^2 )，当每次选择的基准元素都是数组的最大或最小值时，会退化为冒泡排序。
空间复杂度：O(logn)，用于递归调用栈。
优化建议
选择更好的基准元素：可以使用“三数取中”法（Median of Three）来选择基准元素，以减少最坏情况出现的概率。
原地排序：上面的实现使用了额外的列表来存储分割后的部分，可以通过原地分割来减少空间复杂度。
原地快速排序的实现
'''

def quicksort(arr):
    # 如果数组长度小于等于1，则返回数组
    if len(arr) <= 1:
        return arr

    # 选择基准元素，这里选择数组的最后一个元素
    pivot = arr[-1]

    # 分成三个部分：小于基准、等于基准、大于基准
    less = [x for x in arr[:-1] if x <= pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    # 递归地对小于基准和大于基准的部分进行排序
    return quicksort(less) + equal + quicksort(greater)

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print("排序后的数组:", sorted_arr)