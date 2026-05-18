"""Einstein connection: prime coherence to spacetime geometry.

Metric: g_μν = diag(-C, 1/C, r², r² sin²θ)
Ricci scalar: R = -2 dC/dr
Bekenstein-Hawking entropy: S = 1 - C
Cosmological constant: Λ_eff = (1 - C) / C
"""

import math
from typing import Tuple, Dict
from .constants import UNIVERSAL_COHERENCE


def metric_tensor(coherence: float, r: float, theta: float = math.pi/2) -> Dict[str, float]:
    """Return diagonal metric components for given coherence.
    
    g_tt = -C
    g_rr = 1/C
    g_θθ = r²
    g_φφ = r² sin²θ
    """
    return {
        'g_tt': -coherence,
        'g_rr': 1.0 / coherence if coherence != 0 else float('inf'),
        'g_thth': r * r,
        'g_phiphi': r * r * math.sin(theta) ** 2,
    }


def ricci_scalar(coherence_prev: float, coherence_next: float, delta_r: float) -> float:
    """Approximate Ricci scalar from coherence decay.
    
    R ≈ -2 * ΔC / Δr
    Negative R indicates negative curvature (hyperbolic geometry).
    """
    if delta_r == 0:
        return 0.0
    delta_C = coherence_next - coherence_prev
    return -2.0 * delta_C / delta_r


def entropy(coherence: float) -> float:
    """Bekenstein-Hawking entropy from coherence.
    
    S = 1 - C
    Higher coherence → lower entropy (more ordered)
    Lower coherence → higher entropy (more disordered)
    """
    return 1.0 - coherence


def cosmological_constant(coherence: float) -> float:
    """Effective cosmological constant from coherence.
    
    Λ_eff = (1 - C) / C
    At C = 0.5 (universal constant), Λ_eff = 1.0 (normalized)
    At C = 1.0 (perfect coherence), Λ_eff = 0 (vanishes)
    """
    if coherence == 0:
        return float('inf')
    return (1.0 - coherence) / coherence


def green_tao_einstein() -> Dict[int, Dict]:
    """Compute Einstein quantities for Green-Tao progressions."""
    from .lefm import green_tao_coherence
    
    coherences = green_tao_coherence(sigma=0.5)
    # Green-Tao progression primes (approximate radial coordinates)
    progressions = {
        3: [3, 5, 7],
        4: [5, 11, 17, 23],
        5: [5, 11, 17, 23, 29],
        6: [7, 37, 67, 97, 127, 157],
    }
    
    results = {}
    for k, prog in progressions.items():
        C = coherences.get(k, UNIVERSAL_COHERENCE)
        avg_r = sum(math.log(p) for p in prog) / len(prog)
        results[k] = {
            'coherence': C,
            'entropy': entropy(C),
            'cosmological_constant': cosmological_constant(C),
            'avg_log_r': avg_r,
            'metric': metric_tensor(C, avg_r),
        }
    return results