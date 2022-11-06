"""Tests for ipx.py"""
import pytest
import ipx

def test_cleanse():
    """Test cleanse func"""
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

def test_pad_zeroes():
    """Test pad_zeroes func"""
    test_tracks = ['1','42', '7', '333']
    for track in test_tracks:
        if len(track) < 2:
            assert ipx.pad_zeroes(track) == f'0{track}'
        else:
            assert ipx.pad_zeroes(track) == track