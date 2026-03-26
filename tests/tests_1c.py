"""
tests_1c.py

This module contains unit tests for the simple_calculator function defined in
lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum 

def test_simple():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # simple default
    assert max_subarray_sum([100, 1, -3, 4, -1, -1000, 1, -5, 4]) == 102  # simple default

def test_alternate():
    assert max_subarray_sum([1, -1, 10, -10, 100, -100, 1000, -1000]) == 1000

def test_large_numbers():
    assert max_subarray_sum([10**7, -10**16, 10**15]) == 10**15

def test_empty():
    assert max_subarray_sum([]) == 0  

def test_single_element():
    assert max_subarray_sum([1]) == 1  

if __name__ == "__main__":
    pytest.main()
