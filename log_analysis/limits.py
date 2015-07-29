
import re

def limitUrl(log_data, url_regex):
    """ reduce log data by matching certain requirements """
    reduced_data = []
    pattern = re.compile(url_regex)
    for log in log_data:
        if pattern.search(log['request_url']):
            reduced_data.append(log)
    return reduced_data