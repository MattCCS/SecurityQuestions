"""
Script for answering security questions!
"""

import argparse
import base64
import hashlib
import sys


def answer(response):
    h = hashlib.md5(response).digest()
    ans = base64.b16encode(h)[:8].decode('utf-8')
    print(f"Answer: {ans}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="A tool to answer security questions")
    parser.add_argument(
        "response",
        help="The question response.  Must be entered verbatim, will be encoded as UTF-8.")
    return parser.parse_args()


def main():
    args = parse_args()
    answer(args.response.encode('utf-8'))


if __name__ == '__main__':
    main()
