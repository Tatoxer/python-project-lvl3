#!/usr/bin/env python3
import argparse
from page_loader import page

parser = argparse.ArgumentParser(description="Download site page")
parser.add_argument("URL", type=str, help="URL to download")
parser.add_argument("--output", type=str, help="Path to download web-page. "
                                                     "Default: current directory")
args = parser.parse_args()


def main():
    pass


if __name__ == "__main__":
    main()
