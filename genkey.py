#!/usr/bin/env python3
"""
generate_test_secrets.py

Generates fake secrets that match specific Gitleaks rules for testing.
DO NOT use these values in production.
"""

import random
import string

def generate_azure_ad_client_secret():
    """
    Matches the pattern: ([a-zA-Z0-9_~.]{3}\dQ~[a-zA-Z0-9_~.-]{31,34})
    Example: abc1Q~abcdefghijklmnopqrstuvwx.yz12345
    """
    chars_1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_~.'
    chars_2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_~.-'
    
    # Generate the first 3 characters
    part1 = ''.join(random.choices(chars_1, k=3))
    # Generate the digit
    digit = random.choice(string.digits)
    # "Q~" is fixed
    # Generate 31-34 characters
    part2_length = random.randint(31, 34)
    part2 = ''.join(random.choices(chars_2, k=part2_length))
    
    return part1 + digit + "Q~" + part2

def generate_beamer_api_token():
    """
    Matches the pattern: (b_[a-z0-9=_\\-]{44})
    Example: b_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789=_-'
    token_body = ''.join(random.choices(chars, k=44))
    return "b_" + token_body

def generate_bitbucket_client_id():
    """
    Matches the pattern: ([a-z0-9]{32})
    Example: 1234567890abcdef1234567890abcdef
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choices(chars, k=32))

def generate_bitbucket_client_secret():
    """
    Matches the pattern: ([a-z0-9=_\\-]{64})
    Example: 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789=_-'
    return ''.join(random.choices(chars, k=64))

if __name__ == "__main__":
    azure_ad_client_secret = generate_azure_ad_client_secret()
    beamer_api_token = generate_beamer_api_token()
    bitbucket_client_id = generate_bitbucket_client_id()
    bitbucket_client_secret = generate_bitbucket_client_secret()

    print("Fake secrets for Gitleaks testing:")
    print(f"Azure AD Client Secret: {azure_ad_client_secret}")
    print(f"Beamer API Token:      {beamer_api_token}")
    print(f"Bitbucket Client ID:   {bitbucket_client_id}")
    print(f"Bitbucket Client Secret:\n{bitbucket_client_secret}")
