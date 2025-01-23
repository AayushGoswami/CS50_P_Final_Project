import pytest
from project import validate_key, split_uneven, encryption_rule, decryption_rule

def test_validate_key():
    # Test key without '0'
    assert validate_key(12345) == '12345'
    # Test key with '0'
    assert validate_key(12045) != '12045'
    # Test edge case
    assert validate_key(10000) != '10000'

def test_split_uneven():
    text = "Hello World"
    key = "12345"
    # Test splitting with key "12345"
    assert split_uneven(text, key) == ['H', 'ell', 'o', ' Wo', 'r', 'ld']
    # Test edge case with empty text
    assert split_uneven("", key) == []
    # Test edge case with single character text
    assert split_uneven("A", key) == ['A']

def test_encryption_rule():
    key = "12345"
    # Test encryption with length matching key[0]
    assert encryption_rule("H", key) == 'J'
    # Test encryption with length matching key[2]
    assert encryption_rule("ell", key) == 'ipp'
    # Test encryption with default rule
    assert encryption_rule("oW", key) == 't\\'

def test_decryption_rule():
    key = "12345"
    # Test decryption with length matching key[0]
    assert decryption_rule("H", key) == 'F'
    # Test decryption with length matching key[2]
    assert decryption_rule("ell", key) == "ahh"
    # Test decryption with default rule
    assert decryption_rule("oW", key) == "jR"

if __name__ == "__main__":
    pytest.main()
