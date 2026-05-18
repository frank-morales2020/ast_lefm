"""Chowla's conjecture: correlations of Liouville function vanish."""

import math
from typing import List, Tuple
from .sieve import primes_up_to


def liouville(n: int, prime_list: List[int]) -> int:
    """Liouville function λ(n) = (-1)^Ω(n) where Ω(n) = total prime factors."""
    count = 0
    m = n
    for p in prime_list:
        if p * p > m:
            break
        while m % p == 0:
            count += 1
            m //= p
    if m > 1:
        count += 1
    return (-1) ** count


def chowla_correlation(limit: int = 5000) -> float:
    """Average correlation λ(n) * λ(n+1) for n ≤ limit.
    
    Chowla's conjecture predicts this tends to 0 as limit → ∞.
    """
    prime_list = primes_up_to(limit)
    liouville_vals = {n: liouville(n, prime_list) for n in range(2, limit + 1)}
    correlations = [liouville_vals[n] * liouville_vals[n+1] for n in range(2, limit)]
    return sum(correlations) / len(correlations) if correlations else 0.0