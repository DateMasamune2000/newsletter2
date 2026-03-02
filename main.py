#!/usr/bin/env python

import requests
import sys
import certifi
import ssl

from config import load_config

import rss_fetch
import rss_display

commands = {
        "fetch":    lambda argv: rss_fetch.main(argv),
        "display":  lambda argv: rss_display.main(argv),
        }

def main():
    if len(sys.argv) < 2:
        print(f"Incorrect argument list provided", file=sys.stderr)
        print(f"Usage: {sys.argv[0]} command [args]")
        print("Commands:")
        for command in commands.keys():
            print(f"\t- {command}")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd in commands.keys():
        commands[cmd](sys.argv[2:])

if __name__ == "__main__":
    main()
else:
    print("this is not a module.")
