from typing import Generator

def get_prime_number() -> Generator[int, None, None]:
    num = 1
    primes = []
    while True:
        is_searching = True
        while is_searching:
            num += 1
            is_searching = False
            for p in primes:
                if num % p == 0:
                    is_searching = True
                    break
                if p**2 > num:
                    break
        
        primes.append(num)
        yield num

gen = get_prime_number()
print([next(gen) for _ in range(10)])
