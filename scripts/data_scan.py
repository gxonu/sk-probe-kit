#!/usr/bin/env python3
"""Bounded CSV inspection; report aggregates only, never change input data."""
import argparse
import csv
import json
from collections import Counter


def scan(path, limit=1000):
    if limit < 1:
        raise ValueError('max-rows must be positive')
    with open(path, newline='', encoding='utf-8-sig') as stream:
        reader = csv.reader(stream, strict=True)
        header = next(reader, None)
        if not header:
            raise ValueError('CSV header is missing')
        rows = 0
        missing = [0] * len(header)
        seen = set()
        duplicate_rows = 0
        malformed_rows = 0
        truncated = False
        for row in reader:
            if rows == limit:
                truncated = True
                break
            rows += 1
            if len(row) != len(header):
                malformed_rows += 1
            for index in range(len(header)):
                if index >= len(row) or not row[index].strip():
                    missing[index] += 1
            value = tuple(row)
            if value in seen:
                duplicate_rows += 1
            seen.add(value)
    return {
        'rows_scanned': rows, 'truncated': truncated,
        'scope': 'prefix_sample' if truncated else 'all_rows',
        'columns': [{'index': i, 'name': name, 'empty': missing[i]} for i, name in enumerate(header)],
        'duplicate_headers': [key for key, count in Counter(header).items() if count > 1],
        'duplicate_full_rows_in_scan': duplicate_rows,
        'malformed_rows_in_scan': malformed_rows,
        'note': '중복 삭제, 결측 대체, 키 또는 시간대 추정은 하지 않음. 접두 표본은 대표 표본이 아님.'
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv_file')
    p.add_argument('--max-rows', type=int, default=1000)
    args = p.parse_args()
    print(json.dumps(scan(args.csv_file, args.max_rows), ensure_ascii=False, indent=2))
