'''
动态规划（Dynamic Programming, DP）是一种解决复杂问题的方法，通过将问题分解为更小的子问题来解决。
它特别适用于具有重叠子问题和最优子结构性质的问题。动态规划通常通过填充一个表格来存储子问题的解，从而避免重复计算。

动态规划是一种强大的算法设计技术，适用于许多具有重叠子问题和最优子结构性质的问题。
通过将问题分解为更小的子问题，并存储子问题的解，可以高效地解决许多复杂问题
斐波那契数列、最长公共子序列、背包问题和编辑距离是动态规划的经典应用。
'''

'''
斐波那契数列
斐波那契数列是动态规划的经典例子。斐波那契数列的定义如下： 
F(n)=F(n−1)+F(n−2) 其中，F(0)=0 和 F(1)=1。
'''
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 示例
n = 10
print(f"斐波那契数列第 {n} 项: {fibonacci(n)}")

'''
最长公共子序列（LCS）
最长公共子序列问题是指在两个序列中找到最长的公共子序列。动态规划可以高效地解决这个问题。
'''
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# 示例
X = "AGGTAB"
Y = "GXTXAYB"
print(f"最长公共子序列的长度: {lcs(X, Y)}")

'''
背包问题是指在给定的物品中，每个物品都有重量和价值，要求在不超过背包容量的情况下，选择物品使得背包中的总价值最大。
'''
def knapsack(W, weights, values, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# 示例
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)
print(f"最大价值: {knapsack(W, weights, values, n)}")

'''
编辑距离问题是指在两个字符串之间找到最少的编辑操作（插入、删除、替换）将一个字符串转换为另一个字符串。
'''
def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

# 示例
str1 = "sunday"
str2 = "saturday"
print(f"编辑距离: {edit_distance(str1, str2)}")


