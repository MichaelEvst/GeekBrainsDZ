def odd_numbers_generator_without_yield(n):
    return (odd_number for odd_number in range(1, n, 2))
