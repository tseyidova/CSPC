"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.1)



def test_matches_law():
    N0, lam, dt, steps = 1000, 0.4, 0.05, 200
    t = steps * dt
    results = [simulate(N0, lam, dt, steps, seed=s)[-1] for s in range(20)]
    avg = np.mean(results)
    expected = N0 * np.exp(-lam * t)
    assert avg == pytest.approx(expected, rel=0.1)
