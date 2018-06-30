#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function: https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
# author: jmhuang
# email: 946328371@qq.com
# date: 2018/7/1

import sys


def calculate_longest_increasing_subsequence(number, numbers):
    r = [0 for i in range(number)]
    prefix = [0 for i in range(number)]
    for j in range(number):
        if j == 0:
            r[j] = 1
            prefix[j] = 0
            continue
        for i in range(j):
            if numbers[j] > numbers[i]:
                if r[j] < r[i] + 1:
                    r[j] = r[i] + 1
                    prefix[j] = i
        if r[j] == 0:
            r[j] = 1
            prefix[j] = j
    longest_val = 0
    index = 0
    for i, val in enumerate(r):
        if val > longest_val:
            longest_val = val
            index = i
    # addition function to print longest increasing subsequence, no need
    subsequent = []
    while 1:
        subsequent.append(numbers[index])
        if index == prefix[index]:
            break
        else:
            index = prefix[index]
    return longest_val, subsequent[::-1]


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    total_groups = int(lines[0])
    for group in range(total_groups):
        number = int(lines[group * 2 + 1])
        number_list = list(map(int, lines[group * 2 + 2].split()))
        result, subsequent = calculate_longest_increasing_subsequence(number, number_list)
        # print("length:{}, subsequent:{}".format(result, subsequent))
        print(result)