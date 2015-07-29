#!/usr/bin/env python

import log_analysis
from log_analysis import reports
import sys
import os

def main():
    file_in = sys.argv[1]
    if len(sys.argv) > 2:
        depth = int(sys.argv[2])
    else:
        depth = 2

    data = log_analysis.load(file_in)
    paths = reports.pathsViewed(data, depth)

    reports.summary(data)
    reports.reportPretty(paths, 'Paths')


main()
