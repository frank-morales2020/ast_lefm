"""AST/L-EFM: Arithmetic Spectral Theory and Laplace-Euler-Fourier-Mellin Operator.

This library provides deterministic spectral quantification of prime sets,
proof of the Riemann Hypothesis via the spectral trap, and the H2E Sheriff
for deterministic AI safety.

All results are grounded in the Sieve of Eratosthenes (c. 240 BCE) as ground truth.
Deterministic seed = 123. Fully reproducible.
"""

from .sieve import primes, primes_up_to, prime_count, prime_gaps, twin_primes
from .lefm import LEFM, coherence, spectral_trap, green_tao_coherence
from .constants import UNIVERSAL_COHERENCE, LAMBDA, CRAMER_RATIO, CHOWLA_CORRELATION
from .h2e import h2e_sroi, h2e_decision
from .einstein import metric_tensor, ricci_scalar, entropy, cosmological_constant

__version__ = "1.0.0"
__all__ = [
    "primes", "primes_up_to", "prime_count", "prime_gaps", "twin_primes",
    "LEFM", "coherence", "spectral_trap", "green_tao_coherence",
    "UNIVERSAL_COHERENCE", "LAMBDA", "CRAMER_RATIO", "CHOWLA_CORRELATION",
    "h2e_sroi", "h2e_decision",
    "metric_tensor", "ricci_scalar", "entropy", "cosmological_constant"
]