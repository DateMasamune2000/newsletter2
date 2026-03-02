import sys
import os
import stat
import unittest

class Cache:
    def __init__(self, config_obj):
        assert("dir" in config_obj)
        assert("files" in config_obj)

        self._dir = config_obj["dir"]
        self._files = config_obj["files"]

        if self._dir == "DEFAULT":
            self._dir = os.getcwd() + "/newsletter_cache"

        dirmode = None

        try:
            dirmode = os.lstat(self._dir).st_mode
        except FileNotFoundError:
            os.mkdir(self._dir)
            dirmode = os.lstat(self._dir).st_mode

        assert(stat.S_ISDIR(dirmode))

        for f in self._files:
            try:
                filemode = os.lstat(self._files[f]).st_mode
                assert(stat.S_ISREG(filemode))
            except FileNotFoundError:
                pass

    def get_cached_feed(self, feedname):
        if feedname not in self._files.keys():
            return None

        filepath = f"{self._dir}/{self._files[feedname]}"

        if not os.path.exists(filepath):
            return None

        with open(filepath, "r") as feedfile:
            return feedfile.read()

if __name__ == "__main__":
    unittest.main()
