#!/usr/bin/env python3

import os

def test_main():
    """Test that src/main.txt contains the word 'agent'."""
    with open('src/main.txt', 'r') as f:
        content = f.read()
    assert 'agent' in content, "src/main.txt does not contain the word 'agent'"

if __name__ == '__main__':
    test_main()
    print("Test passed!")