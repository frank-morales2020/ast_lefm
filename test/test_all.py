"""Unit tests for AST/L-EFM library."""

import pytest
from ast_lefm.sieve import primes_up_to, prime_gaps, twin_primes
from ast_lefm.lefm import LEFM, coherence, spectral_trap, green_tao_coherence
from ast_lefm.constants import UNIVERSAL_COHERENCE, LAMBDA, CRAMER_RATIO
from ast_lefm.h2e import h2e_sroi, h2e_decision
from ast_lefm.einstein import entropy, cosmological_constant
from ast_lefm.gtt_decay import gtt_decay_law


def test_sieve():
    primes = primes_up_to(100)
    assert len(primes) == 25
    assert primes[0] == 2
    assert primes[-1] == 97


def test_universal_coherence():
    """At σ=0.5, coherence = 0.5 for any prime set."""
    primes_100 = primes_up_to(100)
    assert abs(coherence(primes_100, sigma=0.5) - 0.5) < 1e-6
    
    primes_1000 = primes_up_to(1000)
    assert abs(coherence(primes_1000, sigma=0.5) - 0.5) < 1e-6


def test_spectral_trap():
    """Only σ=0.5 yields normalized magnitude = 1."""
    trap = spectral_trap([0.4, 0.5, 0.6])
    assert trap[0.5] == 1.0
    assert trap[0.4] > 1.0
    assert trap[0.6] < 1.0


def test_gtt_coherence_at_0_5():
    """At σ=0.5, all Green-Tao progressions give 0.5."""
    gtt = green_tao_coherence(sigma=0.5)
    for k in [3, 4, 5, 6]:
        assert abs(gtt[k] - 0.5) < 1e-6


def test_gtt_decay():
    """At σ ≠ 0.5, decay emerges."""
    decay = gtt_decay_law(sigma=0.45)
    values = [decay[k] for k in sorted(decay.keys())]
    # Should be monotonic decreasing
    assert values[0] >= values[-1]
    # k=3 should be highest, k=6 lowest
    assert decay[3] >= decay[6]


def test_lambda_threshold():
    """Λ should be between 0.9 and 0.99."""
    assert 0.95 < LAMBDA < 0.99
    # Specific value from six primes
    assert abs(LAMBDA - 0.9785142874) < 1e-6


def test_cramer_ratio():
    """Cramér ratio from primes ≤ 10000."""
    assert 0.4 < CRAMER_RATIO < 0.5


def test_entropy():
    """Entropy = 1 - coherence."""
    assert entropy(0.5) == 0.5
    assert entropy(0.8) == 0.2
    assert entropy(1.0) == 0.0


def test_cosmological_constant():
    """Λ_eff = (1-C)/C."""
    assert cosmological_constant(0.5) == 1.0
    assert cosmological_constant(1.0) == 0.0
    assert cosmological_constant(0.25) == 3.0
