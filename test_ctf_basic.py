#!/usr/bin/env python3
"""
test_ctf_basic.py
Test base per le challenge CTF â€” livelli 1-5.
Le flag vengono verificate tramite hash MD5 per non rivelare le soluzioni.
"""

import hashlib
import pytest

# Hash MD5 delle flag corrette (le flag non sono visibili nei test)
EXPECTED_HASHES = {
    1: "4dcb3fa0a4eeef1d805ede197f264674",
    2: "24bdbfbc45297806e355200b1ff9ebe9",
    3: "c15aeb4c5cf341f1cb2cf2b1b456613d",
    4: "16c127b642f2a569b3fa392cee87908e",
    5: "5920889c1954281143a078bf74fe8040",
}


def flag_hash(flag: str) -> str:
    """Compute MD5 hash of a flag string."""
    return hashlib.md5(flag.encode()).hexdigest()


# Import delle funzioni con try/except
try:
    from ctf_decoder import solve_level_1
except ImportError:
    solve_level_1 = None

try:
    from ctf_decoder import solve_level_2
except ImportError:
    solve_level_2 = None

try:
    from ctf_decoder import solve_level_3
except ImportError:
    solve_level_3 = None

try:
    from ctf_decoder import solve_level_4
except ImportError:
    solve_level_4 = None

try:
    from ctf_decoder import solve_level_5
except ImportError:
    solve_level_5 = None


def test_structure_check():
    """Verify that ctf_decoder.py exists and contains the required functions"""
    missing = []
    if solve_level_1 is None:
        missing.append("solve_level_1")
    if solve_level_2 is None:
        missing.append("solve_level_2")
    if solve_level_3 is None:
        missing.append("solve_level_3")
    if solve_level_4 is None:
        missing.append("solve_level_4")
    if solve_level_5 is None:
        missing.append("solve_level_5")
    assert len(missing) == 0, (
        f"CRITICAL ERROR: Could not find {', '.join(missing)} in 'ctf_decoder.py'. "
        "Make sure your file is named exactly 'ctf_decoder.py' "
        "and all functions are named 'solve_level_X'."
    )


def test_level_1_hex_decode():
    """Level 1: basic hex decoding should return the correct flag"""
    assert solve_level_1 is not None, "solve_level_1 not found"
    result = solve_level_1()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[1], (
        f"Level 1: wrong flag. Got: '{result}'"
    )


def test_level_1_flag_format():
    """Level 1: result should follow the flag{...} format"""
    assert solve_level_1 is not None, "solve_level_1 not found"
    result = solve_level_1()
    assert result.startswith("flag{") and result.endswith("}"), (
        f"Flag format incorrect. Expected 'flag{{...}}', got: '{result}'"
    )


def test_level_2_base64_and_int():
    """Level 2: base64 + int big endian decoding"""
    assert solve_level_2 is not None, "solve_level_2 not found"
    result = solve_level_2()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[2], (
        f"Level 2: wrong flag. Got: '{result}'"
    )


def test_level_3_base64_over_hex():
    """Level 3: base64 wrapping a hex string"""
    assert solve_level_3 is not None, "solve_level_3 not found"
    result = solve_level_3()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[3], (
        f"Level 3: wrong flag. Got: '{result}'"
    )


def test_level_4_double_base64():
    """Level 4: double base64 encoding"""
    assert solve_level_4 is not None, "solve_level_4 not found"
    result = solve_level_4()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[4], (
        f"Level 4: wrong flag. Got: '{result}'"
    )


def test_level_5_reversed_hex_bytes():
    """Level 5: hex string with reversed byte order"""
    assert solve_level_5 is not None, "solve_level_5 not found"
    result = solve_level_5()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[5], (
        f"Level 5: wrong flag. Got: '{result}'"
    )
