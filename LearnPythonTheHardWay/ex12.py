# -*- coding: utf-8 -*-
#Exercise 12: Prompting People

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# 以下代码源于
# AndroidShareGroup - ASG 538266272 的
# 北京 - Yat3s 的关于斐波那契数列的算法提问
# def fff(n):
#     sum_n = 0
#     i = 1
#     n1 = 1
#     n2 = 1
#     while i <= n:
#         if(i == 1 or i == 2):
#             sum_n = 1
#             i += 1
#             continue
#         sum_n = n1 + n2
#         n1 = n2
#         n2 = sum_n
#         i += 1
#     return sum_n
#
# print fff(100000)
