#!/usr/bin/env python3
import sys

import general_superstaq.check

if __name__ == "__main__":
    skip_args = ["--skip", "requirements", "build_docs", "--"]
    exit(general_superstaq.check.all_.run(*skip_args, *sys.argv[1:]))
