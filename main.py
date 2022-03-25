fib_nums = dict({0: 0, 1: 1})


def fibonacci(n):
    # Checks if what we need has already been computed
    # if so then simply return that value
    if n in fib_nums:
        return fib_nums.get(n)

    # Stores the value in the dictionary so we don't have to
    # recalculate when calculating other fibs that use this
    fib_nums[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_nums[n]


if __name__ == "__main__":
    print(fibonacci(int(input())))