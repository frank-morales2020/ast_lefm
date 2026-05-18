"""Sieve of Eratosthenes - Ground Truth Prime Enumeration.

Invented by Eratosthenes of Cyrene (276-194 BCE).
Deterministic. 100% accurate. No false positives. No false negatives.
"""

import math
from typing import List, Set, Tuple, Generator

SEED = 123  # Fixed deterministic seed for all computations


def primes_up_to(limit: int) -> List[int]:
    """Return list of all primes ≤ limit using Sieve of Eratosthenes.
    
    Time complexity: O(N log log N)
    Space complexity: O(N)
    Accuracy: 100% deterministic.
    """
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return [p for p in range(2, limit + 1) if sieve[p]]


def primes(limit: int = 10000) -> List[int]:
    """Default prime set up to 10,000 (1229 primes). Ground truth cache."""
    _PRIMES_CACHE = {}
    if limit not in _PRIMES_CACHE:
        _PRIMES_CACHE[limit] = primes_up_to(limit)
    return _PRIMES_CACHE[limit]


def prime_count(limit: int) -> int:
    """Return π(limit) = number of primes ≤ limit."""
    return len(primes_up_to(limit))


def prime_gaps(limit: int = 10000) -> List[int]:
    """Return list of gaps between consecutive primes ≤ limit."""
    p_list = primes_up_to(limit)
    return [p_list[i+1] - p_list[i] for i in range(len(p_list) - 1)]


def twin_primes(limit: int = 10000) -> List[Tuple[int, int]]:
    """Return list of twin prime pairs (p, p+2) both ≤ limit."""
    p_set = set(primes_up_to(limit))
    return [(p, p+2) for p in p_set if p+2 in p_set]


def green_tao_progressions() -> dict:
    """Known Green-Tao arithmetic progressions of primes."""
    return {
        3: [3, 5, 7],
        4: [5, 11, 17, 23],
        5: [5, 11, 17, 23, 29],
        6: [7, 37, 67, 97, 127, 157],
    }