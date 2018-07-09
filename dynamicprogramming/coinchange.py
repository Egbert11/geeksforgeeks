#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function: https://practice.geeksforgeeks.org/problems/coin-change/0
# author: jmhuang
# email: 946328371@qq.com
# date: 2018/7/1

import sys

global matrix

def calculate_coin_change(number, number_list):
    global matrix
    if number == 0:
        return 0
    if not number_list:
        return 0
    number_list.sort()
    if number < number_list[0]:
        return 0
    if matrix[number][number_list[0]] != -1:
        return matrix[number][number_list[0]]
    result = 0
    for i, num in enumerate(number_list):
        if number < num:
            break
        elif number == num:
            result += 1
        else:
            result += calculate_coin_change(number - num, number_list[i:])
    matrix[number][number_list[0]] = result
    return result



if __name__ == "__main__":
    lines = sys.stdin.readlines()
    total_groups = int(lines[0])
    for group in range(total_groups):
        number_len = int(lines[group * 3 + 1])
        global matrix
        number_list = list(map(int, lines[group * 3 + 2].split()))
        total = int(lines[group * 3 + 3])
        matrix = [[-1 for i in range(total + 1)] for i in range(total + 1)]
        result = calculate_coin_change(total, number_list)
        # for each in matrix:
        #     print each
        print(result)