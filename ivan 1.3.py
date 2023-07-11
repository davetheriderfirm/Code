def sum_n_2(n):
    if n <= 0:
        return 0
    return(n+sum_n_2(n-2))

print(sum_n_2(13))