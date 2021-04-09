def odd_num_gen_without_yield(n)
    return (odd_num for odd_num in range(1, n, 2))
