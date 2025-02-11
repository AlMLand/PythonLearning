def count_primes(num: int) -> int:
    if num < 2:
        return 0

    count = 0
    for n in range(2, num + 1):
        if is_prime(n):
            count += 1

    return count


def is_prime(n: int) -> bool:
    how_times = 1
    for i in range(2, n):
        if n % i == 0:
            how_times += 1

    return how_times == 1


#####
print(count_primes(100))
