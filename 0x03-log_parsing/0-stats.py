#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics.
"""
import sys


def print_statistics(lines_count, total_file_size, status_code_counts):
    """Print the status code"""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def main():
    """Entry point of the function"""
    lines_count = 0
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                          403: 0, 404: 0, 405: 0, 500: 0}

    try:
        """Read stdin line by line"""
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) >= 6 and parts[-1].isdigit():
                file_size = int(parts[-1])
                total_file_size += file_size
                status_code = int(parts[-2])
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            lines_count += 1

            if lines_count % 10 == 0:
                print_statistics(lines_count, total_file_size,
                                 status_code_counts)

    except KeyboardInterrupt:
        print_statistics(lines_count, total_file_size, status_code_counts)


if __name__ == "__main__":
    main()
