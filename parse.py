#!/usr/bin/env python

import log_analysis 
import sys

def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    log_format = sys.argv[3]
    line_pattern = getattr(log_analysis.LogFormats, log_format)

    log_data = log_analysis.parse(file_in, line_pattern)
    log_analysis.save(log_data, file_out)

main()

