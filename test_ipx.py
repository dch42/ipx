"""Tests for ipx.py"""
import pytest
import ipx

def test_cleanse():
    """Ensure """
    illegal_chars = ['/','\\','<','>','*','?','|',':']
    test_vals = [
        'Band1 / Band2',
        'Band?',
        'The Album: Special Edition',
        '()*\\&|//??:><:!@#'
    ]
    for val in test_vals:
        cleansed = ipx.cleanse(val)
        if val == test_vals[0]:
            assert cleansed == 'Band1 - Band2'
        if val == test_vals[2]:
            assert cleansed == 'The Album- Special Edition'
        for c in cleansed:
            assert c not in illegal_chars 
