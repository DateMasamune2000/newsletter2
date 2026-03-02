#!/usr/bin/env python

import requests
import sys
import certifi
import ssl

from config import load_config


def main():
    print(ssl.get_default_verify_paths())
    # TODO: implement default config file location
    assert len(sys.argv) == 2

    config = load_config(sys.argv[1])
    for feed in config["feeds"]:

        # TODO: check configuration correctness
        assert("url" in feed.keys())

        response = requests.get(feed["url"], verify=certifi.where())
        
        # TODO: handle failed requests or requests with bad mime types
        print(f"content type {response.headers['content-type']}")
        assert(response.headers["content-type"].split(';')[0]
               in ["application/xml", "application/rss+xml"])

        # TODO: handle non UTF-8 character sets
        assert(response.encoding == "utf-8")

        raw_content = response.text

        print(raw_content)

if __name__ == "__main__":
    main()
else:
    print("this is not a module.")
