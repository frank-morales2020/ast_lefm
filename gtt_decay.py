"""Green-Tao theorem quantification: coherence decay law.

At σ ≠ 0.5, longer progressions show lower coherence.
At σ = 0.5, all progressions show universal coherence = 0.5.
"""

from .lefm import LEFM
from .sieve import green_tao_progressions


def gtt_decay_law(sigma: float = 0.45) -> dict:
    """Compute coherence for Green-Tao progressions at given σ.
    
    For σ slightly off the critical line (e.g., 0.45 or 0.55),
    a monotonic decay emerges: k=3 (highest) → k=6 (lowest).
    
    This decay is the spectral signature of GTT that AST/L-EFM reveals.
    """
    progressions = green_tao_progressions()
    operator = LEFM()
    
    results = {}
    for k, prog in progressions.items():
        # raw_coherence (no scaling) at σ ≠ 0.5
        coh = operator.raw_coherence(prog, sigma=sigma)
        results[k] = coh
    
    return results


def print_decay_law(sigma: float = 0.45):
    """Print formatted decay law for GTT."""
    decay = gtt_decay_law(sigma)
    print(f"\nGreen-Tao Coherence Decay at σ = {sigma}")
    print("-" * 40)
    for k in sorted(decay.keys()):
        print(f"k = {k}: coherence = {decay[k]:.6f}")
    print("-" * 40)
    
    # Check monotonic decay
    values = [decay[k] for k in sorted(decay.keys())]
    if all(values[i] >= values[i+1] for i in range(len(values)-1)):
        print("✓ Monotonic decay confirmed (longer progressions = lower coherence)")
    else:
        print("✗ Non-monotonic (check σ value)")