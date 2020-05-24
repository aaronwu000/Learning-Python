def recursive_climbStairs(n: int):

    if n < 3:
        return n
    else:
        return recursive_climbStairs(n-1) + recursive_climbStairs(n-2)
print(recursive_climbStairs(8))