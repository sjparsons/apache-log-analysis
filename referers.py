#!/usr/bin/env python

import log_analysis
from log_analysis import reports
import sys
import os

def main():
    file_in = sys.argv[1]

    data = log_analysis.load(file_in)
    referers = reports.referers(data)

    reports.summary(data)
    reports.reportPretty(referers, 'Referers')


main()
