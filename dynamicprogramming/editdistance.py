#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function: https://practice.geeksforgeeks.org/problems/edit-distance/0
# author: jmhuang
# email: 946328371@qq.com
# date: 2018/7/1

import sys


def solution(len1, len2, str1, str2):
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    if len(str1) > len(str2):
        len1, len2 = len2, len1
        str1, str2 = str2, str1
    arr = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    for i in range(len1 + 1):
        arr[i][0] = i
    for i in range(len2 + 1):
        arr[0][i] = i
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1

    # for i in arr:
    #     print i
    return arr[len1][len2]


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    total_groups = int(lines[0])
    for group in range(total_groups):
        lens = list(map(int, lines[group * 2 + 1].split()))
        strs = list(lines[group * 2 + 2].split())
        result = solution(lens[0], lens[1], strs[0], strs[1])
        print(result)