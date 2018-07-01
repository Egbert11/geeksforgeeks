#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function: https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0
# author: jmhuang
# email: 946328371@qq.com
# date: 2018/7/1

import sys


# Time: O(m*n), Space: O(m * n)
def calculate_longest_common_subsequence_v1(len1, len2, list1, list2):
    arr = [[0 for i in range(len2)] for j in range(len1)]
    for i in range(len1):
        for j in range(len2):
            val = 1 if list1[i] == list2[j] else 0
            if val:
                if 0 in (i, j):
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                if i == 0 and j == 0:
                    arr[i][j] = 0
                elif i == 0:
                    arr[i][j] = arr[i][j - 1]
                elif j == 0:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    # use backtracking to find lcs string
    subsequence = []
    i, j = len1 - 1, len2 - 1
    while True:
        if list1[i] == list2[j]:
            subsequence.append(list1[i])
            i -= 1
            j -= 1
        else:
            if i == 0 and j == 0:
                break
            elif i == 0:
                j -= 1
            elif j == 0:
                i -= 1
            else:
                if arr[i - 1][j] > arr[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
        if len(subsequence) == arr[len1 - 1][len2 - 1]:
            break
    return arr[len1 - 1][len2 - 1], subsequence[::-1]


# Time: O(m*n), Space: O(min{m, n})
def calculate_longest_common_subsequence_v2(len1, len2, list1, list2):
    arr = [0] * (min(len1, len2) + 1)
    if len2 > len1:
        len2, len1 = len1, len2
        list2, list1 = list1, list2
    cache = 0
    for i in range(len1):
        for j in range(1, len2 + 1):  # inner should be smaller
            val = 1 if list1[i] == list2[j - 1] else 0
            temp = arr[j]
            if val:
                if j == 1:
                    arr[j] = arr[j - 1] + val
                else:
                    arr[j] = cache + val
            else:
                # temp = arr[j]  # cache, avoid override by next loop
                arr[j] = max(arr[j], arr[j - 1])
            cache = temp  # cache, avoid override by next loop
        print(arr)
    # use backtracking to find lcs string(really tricky and open minded)
    subsequence = []


    return arr[-1]


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    total_groups = int(lines[0])
    for group in range(total_groups):
        lens = list(map(int, lines[group * 3 + 1].split()))
        list1 = list(lines[group * 3 + 2].strip())
        list2 = list(lines[group * 3 + 3].strip())
        # result, subsequence = calculate_longest_common_subsequence_v1(lens[0], lens[1], list1, list2)
        result = calculate_longest_common_subsequence_v2(lens[0], lens[1], list1, list2)
        # print("length:{}, subsequence:{}".format(result, subsequence))
        print(result)