"""Universal constants derived from AST/L-EFM framework.

All constants are computed deterministically from the Sieve of Eratosthenes.
No empirical tuning. No free parameters.
"""

import math
from .sieve import primes_up_to

# Universal Spectral Constant: at σ = 0.5, coherence = 0.5 for every non-empty prime set
UNIVERSAL_COHERENCE = 0.5

# Safety threshold Λ computed from first six primes {2,3,5,7,11,13}
# Λ = 1 - ∏_{p≤13} (1 - p^{-1/2})
_I = math.prod(1.0 - p**(-0.5) for p in [2, 3, 5, 7, 11, 13])
LAMBDA = 1.0 - _I  # ≈ 0.9785142874

# Cramér ratio from prime gaps up to 10,000
def _compute_cramer_ratio():
    primes = primes_up_to(10000)
    max_gap = max(primes[i+1] - primes[i] for i in range(len(primes)-1))
    log_p_max = math.log(primes[-1])
    return max_gap / (log_p_max ** 2)

CRAMER_RATIO = _compute_cramer_ratio()  # ≈ 0.424626

# Chowla correlation from Liouville function
def _compute_chowla_correlation():
    from .chowla import chowla_correlation
    return chowla_correlation()

CHOWLA_CORRELATION = _compute_chowla_correlation()  # ≈ 0.014806