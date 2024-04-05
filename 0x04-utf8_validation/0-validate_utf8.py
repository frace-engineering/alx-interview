#!/usr/bin/python3
"""Validate utf-8 character"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: A list of integers, each representing 1 byte of data

    Returns:
    - True if data is a valid UTF-8 encoding, else False
    """
    bytes_to_follow = 0
    """Number of bytes to follow for the current character"""

    for byte in data:
        """Check if this byte is the start of a new character"""
        if bytes_to_follow == 0:
            """
            Determine the number of bytes to follow based on the
            first few bits of this byte
            """
            if byte >> 7 == 0b0:
                """1-byte character"""
                bytes_to_follow = 0
            elif byte >> 5 == 0b110:
                """2-byte character"""
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                """3-byte character"""
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                """4-byte character"""
                bytes_to_follow = 3
            else:
                """Invalid start of a character"""
                return False
        else:
            """Check if this byte is a continuation byte"""
            if byte >> 6 == 0b10:
                bytes_to_follow -= 1
            else:
                """Invalid continuation byte"""
                return False

    """Check if all continuation bytes were found"""
    return bytes_to_follow == 0
