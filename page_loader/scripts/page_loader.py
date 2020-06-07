#!/usr/bin/env python3
import argparse
from page_loader import page

parser = argparse.ArgumentParser(description="Download site page")
parser.add_argument("url", type=str, help="URL to download")
parser.add_argument("--output", type=str, help="Path to download web-page. "
                                               "Default: current directory")
args = parser.parse_args()


def main():
    url = args.url
    if args.output is None:
        page.download_page(url)
    else:
        page.download_page(url, args.output)


if __name__ == "__main__":
    main()
