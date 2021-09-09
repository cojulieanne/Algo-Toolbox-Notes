"""
------------------------------------------------------
Last Digit of a Large Fibonacci Number

(c) 2018 Julie Co, Manila, Philippines
Coursera Algorithmic Toolbox - UC San Diego & HSE
Week 2 - Algorthmic Warmup - Last Digit of a Large Fibonacci Number
------------------------------------------------------
"""


# Iterative Fibonacci Function -- Last Digit Retrieval
# Note that loop is used instead of recursion because of Python recursion depth limit of 1000
# Change depth limit by sys.setrecursionlimit(n)

def fib(n):

    prev = 0
    curr = 1

    # Initialize Fibonacci memo. Fibonacci last digit is expected to repeat a pattern after n indices
    pattern = []

    # Memoize the (Fib_n, Fib_(n+1)). Once the first pair (0,1) appears after some n terms, the cycle is complete.
    pattern.append((0, 1))

    ##print("{}: {}".format(0, pattern[-1]))

    for i in range(n):
        temp = curr
        curr = (curr + prev) % 10
        prev = temp % 10

        if (prev, curr) in pattern:     # Stop memoization after a Fibonacci pair repeats in the memo

            # Index of the last digit of the nth Fibonacci term
            index = n % len(pattern)

            return pattern[index][0]

        else:

            # Append Fibonacci pair while cycle is not complete
            pattern.append((prev, curr))

        ##print("{}: {}".format(i+1, pattern[-1]))

    # In pair (a,b) for index n, a is always the las digit of the nth Fibonacci term. b is for the (n+1)th term.
    return prev


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
