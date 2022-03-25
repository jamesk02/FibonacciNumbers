if __name__ == "__main__":
    n = int(input())

    fib_nums = [0, 1]

    for x in range(2, n + 1):
        fib_nums.append(fib_nums[x - 1] + fib_nums[x - 2])

    print(fib_nums[n])