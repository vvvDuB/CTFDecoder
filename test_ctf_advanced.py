#!/usr/bin/env python3
"""
test_ctf_advanced.py
Test avanzati per le challenge CTF â€” livelli 6-11.
Le flag vengono verificate tramite hash MD5 per non rivelare le soluzioni.
"""

import hashlib
import pytest

# Hash MD5 delle flag corrette (le flag non sono visibili nei test)
EXPECTED_HASHES = {
    6: "da961cfff21713b2d3940870a6cfd8c0",
    7: "821a54ce7a759e91db122e129ccd9ee3",
    8: "1f0149ae77c0289a0c27322bfec9ed33",
    9: "05ca944722a2b9804161d2a39b0b9405",
    10: "1484d9e1ed054fbc8a600486bba9fd64",
    11: "a56e92c7b56f7567c88fb5c174db2664",
}


def flag_hash(flag: str) -> str:
    """Compute MD5 hash of a flag string."""
    return hashlib.md5(flag.encode()).hexdigest()


# Import delle funzioni con try/except
try:
    from ctf_decoder import solve_level_6
except ImportError:
    solve_level_6 = None

try:
    from ctf_decoder import solve_level_7
except ImportError:
    solve_level_7 = None

try:
    from ctf_decoder import solve_level_8
except ImportError:
    solve_level_8 = None

try:
    from ctf_decoder import solve_level_9
except ImportError:
    solve_level_9 = None

try:
    from ctf_decoder import solve_level_10
except ImportError:
    solve_level_10 = None

try:
    from ctf_decoder import solve_level_11
except ImportError:
    solve_level_11 = None


def test_structure_check():
    """Verify that ctf_decoder.py contains the advanced level functions"""
    missing = []
    if solve_level_6 is None:
        missing.append("solve_level_6")
    if solve_level_7 is None:
        missing.append("solve_level_7")
    if solve_level_8 is None:
        missing.append("solve_level_8")
    if solve_level_9 is None:
        missing.append("solve_level_9")
    if solve_level_10 is None:
        missing.append("solve_level_10")
    if solve_level_11 is None:
        missing.append("solve_level_11")
    assert len(missing) == 0, (
        f"CRITICAL ERROR: Could not find {', '.join(missing)} in 'ctf_decoder.py'. "
        "Make sure all functions are named 'solve_level_X'."
    )


def test_level_6_two_byte_padding():
    """Level 6: each char encoded as 2-byte big endian in hex"""
    assert solve_level_6 is not None, "solve_level_6 not found"
    result = solve_level_6()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[6], (
        f"Level 6: wrong flag. Got: '{result}'"
    )


def test_level_7_triple_encoding():
    """Level 7: three layers of encoding (hex â†’ base64 â†’ hex)"""
    assert solve_level_7 is not None, "solve_level_7 not found"
    result = solve_level_7()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[7], (
        f"Level 7: wrong flag. Got: '{result}'"
    )


def test_level_8_alternating_encoding():
    """Level 8: alternating hex/base64 blocks"""
    assert solve_level_8 is not None, "solve_level_8 not found"
    result = solve_level_8()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[8], (
        f"Level 8: wrong flag. Got: '{result}'"
    )


def test_level_9_caesar_base64():
    """Level 9: Caesar cipher wrapped in base64"""
    assert solve_level_9 is not None, "solve_level_9 not found"
    result = solve_level_9()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[9], (
        f"Level 9: wrong flag. Got: '{result}'"
    )


def test_level_10_multi_layer():
    """Level 10: multi-layer with endianness and Caesar"""
    assert solve_level_10 is not None, "solve_level_10 not found"
    result = solve_level_10()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[10], (
        f"Level 10: wrong flag. Got: '{result}'"
    )


def test_level_11_final_boss():
    """Level 11: final boss â€” Morse â†’ hex â†’ binary â†’ base64 â†’ Caesar"""
    assert solve_level_11 is not None, "solve_level_11 not found"
    try:
        result = solve_level_11()
    except FileNotFoundError:
        pytest.fail(
            "Level 11: file 'challenge_final_boss.txt' not found. "
            "Make sure it is in the same folder as your code."
        )
    assert isinstance(result, str), f"Expected str, got {type(result)}"
    assert flag_hash(result) == EXPECTED_HASHES[11], (
        f"Level 11: wrong flag. Got: '{result}'"
    )


def test_all_flags_format():
    """Verify that all flags from levels 6-11 follow the flag{...} format"""
    solvers = [
        ("Level 6", solve_level_6),
        ("Level 7", solve_level_7),
        ("Level 8", solve_level_8),
        ("Level 9", solve_level_9),
        ("Level 10", solve_level_10),
        ("Level 11", solve_level_11),
    ]
    for name, solver in solvers:
        if solver is None:
            pytest.skip(f"{name} not implemented yet")
        try:
            result = solver()
        except FileNotFoundError:
            pytest.skip(f"{name}: challenge file not found")
        assert result.startswith("flag{") and result.endswith("}"), (
            f"{name}: flag format incorrect. Expected 'flag{{...}}', got: '{result}'"
        )


def test_all_flags_are_unique():
    """Verify that no two levels return the same flag"""
    solvers = [
        solve_level_6, solve_level_7, solve_level_8,
        solve_level_9, solve_level_10, solve_level_11,
    ]
    results = []
    for solver in solvers:
        if solver is None:
            pytest.skip("Not all functions implemented yet")
        try:
            results.append(solver())
        except FileNotFoundError:
            pytest.skip("Challenge file not found")
    assert len(results) == len(set(results)), (
        "Some levels return the same flag â€” are you sure each function solves its own level?"
    )
