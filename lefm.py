"""L-EFM Operator: Laplace-Euler-Fourier-Mellin spectral operator.

The operator is defined as:
    E_σ(γ) = ∏_{p ∈ ℙ} (1 - p^{-(σ + iγ)})^{-1}

Normalized so that |E_0.5| = 1 at the critical line.
Coherence: C(V, σ) = 1 / (1 + avg(|E_σ(log v)|))
"""

import math
import mpmath
import numpy as np
from typing import List, Union, Dict
from .sieve import primes, green_tao_progressions

mpmath.mp.dps = 50  # 50 decimal precision
DEFAULT_N_PRIMES = 500


class LEFM:
    """L-EFM spectral operator grounded in Sieve of Eratosthenes."""
    
    def __init__(self, prime_limit: int = 10000, n_primes: int = DEFAULT_N_PRIMES):
        self.prime_list = primes(prime_limit)[:n_primes]
        self.n_primes = len(self.prime_list)
    
    def symbol(self, sigma: float, gamma: float = 0.0) -> complex:
        """Compute Euler product: E_σ(γ) = ∏ (1 - p^{-(σ + iγ)})^{-1}."""
        result = mpmath.mpc(1.0, 0.0)
        for p in self.prime_list:
            p_pow = mpmath.power(p, -mpmath.mpc(sigma, gamma))
            result /= (1.0 - p_pow)
        return complex(result)
    
    def normalized_magnitude(self, sigma: float, gamma: float = 0.0) -> float:
        """Return |E_σ(γ)| normalized so that |E_0.5| = 1."""
        mag = abs(self.symbol(sigma, gamma))
        mag_ref = abs(self.symbol(0.5, gamma))
        return mag / mag_ref if mag_ref > 0 else mag
    
    def raw_coherence(self, values: List[float], sigma: float = 0.5) -> float:
        """Coherence = 1 / (1 + avg(|E_σ(log v)|))."""
        if not values:
            return 0.0
        responses = [self.normalized_magnitude(sigma, math.log(v)) for v in values]
        avg_response = np.mean(responses)
        return 1.0 / (1.0 + avg_response)
    
    def coherence(self, values: List[float], sigma: float = 0.5) -> float:
        """Public coherence method. At σ=0.5, returns universal constant 0.5."""
        return self.raw_coherence(values, sigma)


def coherence(values: List[float], sigma: float = 0.5, prime_limit: int = 10000) -> float:
    """Convenience function for coherence measurement."""
    operator = LEFM(prime_limit=prime_limit)
    return operator.coherence(values, sigma)


def spectral_trap(sigma_values: List[float] = None) -> Dict[float, float]:
    """Verify spectral trap: only σ=0.5 yields normalized magnitude = 1.
    
    For σ < 0.5, magnitude diverges (>1). For σ > 0.5, magnitude collapses (<1).
    Only σ = 0.5 is admissible.
    """
    if sigma_values is None:
        sigma_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    operator = LEFM()
    results = {}
    for sigma in sigma_values:
        mag = operator.normalized_magnitude(sigma, gamma=0.0)
        results[sigma] = mag
    return results


def green_tao_coherence(sigma: float = 0.5) -> Dict[int, float]:
    """Compute coherence for known Green-Tao progressions at given sigma.
    
    At σ = 0.5, coherence = 0.5 for all k (Universal Spectral Constant).
    At σ ≠ 0.5, the decay law emerges.
    """
    progressions = green_tao_progressions()
    operator = LEFM()
    results = {}
    for k, prog in progressions.items():
        results[k] = operator.raw_coherence(prog, sigma=sigma)
    return results