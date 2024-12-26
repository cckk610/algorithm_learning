'''
KMP算法（Knuth-Morris-Pratt Algorithm）是一种用于在文本中查找模式的高效字符串匹配算法。
它通过预处理模式字符串，构建部分匹配表（也称为前缀函数或失配函数），从而避免在匹配过程中重复扫描文本。

KMP算法的基本思想
部分匹配表（前缀函数）：部分匹配表记录了模式字符串的前缀和后缀的最长公共元素的长度。通过这个表，可以在匹配失败时快速跳过一些字符，从而提高匹配效率。
匹配过程：在匹配过程中，如果遇到不匹配的字符，可以根据部分匹配表跳过一些字符，而不是重新从头开始匹配。

时间复杂度
预处理部分匹配表：O(m)，其中 m 是模式字符串的长度。
匹配过程：O(n)，其中 n 是文本的长度。
因此，KMP算法的总时间复杂度为 O(n+m)，在实际应用中非常高效。
'''

def compute_lps(pattern):
    """
    计算部分匹配表（前缀函数）
    """
    lps = [0] * len(pattern)
    length = 0  # 前缀的长度
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    """
    KMP字符串匹配算法
    """
    lps = compute_lps(pattern)
    i = 0  # text的索引
    j = 0  # pattern的索引

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            print(f"找到匹配位置: {i - j}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# 示例
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)
