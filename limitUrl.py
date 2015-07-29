#!/usr/bin/env python

import log_analysis
from log_analysis import limits
import sys

def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    url_regex = sys.argv[3]

    data = log_analysis.load(file_in)
    data = limits.limitUrl(data, url_regex)

    reports.summary(data)
    log_analysis.save(data, file_out)


main()
