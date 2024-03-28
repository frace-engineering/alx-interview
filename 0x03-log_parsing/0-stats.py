#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import signal


""" Initialize global variables to store metrics """
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                      404: 0, 405: 0, 500: 0}
lines_processed = 0


def print_metrics():
    """Pring matrics"""
    global total_file_size
    global status_code_counts
    global lines_processed
    print("File size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0 and isinstance(status_code, int):
            print(f"{status_code}: {count}")
    """ Reset metrics """
    """total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                          404: 0, 405: 0, 500: 0}
    lines_processed = 0"""


def process_line(line):
    global total_file_size
    global status_code_counts
    global lines_processed
    try:
        parts = line.split()
        if len(parts) >= 6:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
    except ValueError:
        pass


def signal_handler(signal, frame):
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line.strip())
        lines_processed += 1
        if lines_processed % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    pass


print_metrics()
