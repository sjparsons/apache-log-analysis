#!/usr/bin/env python

import log_analysis
from log_analysis import reports
import sys

def main():
    file_in = sys.argv[1]

    data = log_analysis.load(file_in)
    hours = reports.hours(data)

    reports.summary(data)
    reports.reportPretty(hours, 'Hours')


main()
