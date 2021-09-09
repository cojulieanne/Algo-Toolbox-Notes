"""
------------------------------------------------------
Simple Fibonacci Recursive function (starting from 0,1)

(c) 2018 Julie Co, Manila, Philippines
Coursera Algorithmic Toolbox - UC San Diego & HSE
Week 2 - Algorthmic Warmup - Fibonacci Number
------------------------------------------------------
"""

# Fibonacci Function


def calc_fib(n):
    prev = 0
    curr = 1
    for i in range(n):
        temp = curr
        curr = prev+curr
        prev = temp
    return prev


n = int(input())
print(calc_fib(n))
