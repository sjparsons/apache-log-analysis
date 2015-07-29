
import datetime

# Helper functions

ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S"

def _trunc_at(s, d, n=3):
    "Returns string, s, truncated at the n'th (3rd by default) \
    occurrence of the delimiter, d."
    return d.join(s.split(d)[:n])

# General reporting functions

def reportPretty(result, name):
    for key in sorted(result):
        print "{0: >12}  {1:}".format(result[key], key)

def reportCsv(result, name):
    for key in sorted(result):
        print key + "," + result[key]

def summary(data):
    print "Log data has %d entries" % len(data)
    print "=" * 80

# Reports


def pathsViewed(log_data, depth=4):
    paths = {}
    for visit in log_data:
        path = _trunc_at(visit['request_url'],'/',depth)
        if path in paths:
            paths[path] += 1
        else:
            paths[path] = 1

    return paths


def referers(log_data):
    referers = {}
    for visit in log_data:
        referer = visit['request_header_referer']
        if referer in referers:
            referers[referer] += 1
        else:
            referers[referer] = 1
            
    return referers



def hours(log_data):
    hours = {}
    for visit in log_data:
        time = datetime.datetime.strptime(visit['time_received_isoformat'], ISO8601_FORMAT)
        hour = datetime.datetime.strftime(time,'%Y-%m-%d %H')
        if hour in hours:
            hours[hour] += 1
        else:
            hours[hour] = 1
            
    return hours

def hoursTotals(log_data):
    hours = {}
    for visit in log_data:
        time = datetime.datetime.strptime(visit['time_received_isoformat'], ISO8601_FORMAT)
        hour = datetime.datetime.strftime(time,'%H')
        if hour in hours:
            hours[hour] += 1
        else:
            hours[hour] = 1
            
    return hours


def minutes(log_data):
    mins = {}
    for visit in log_data:
        time = datetime.datetime.strptime(visit['time_received_isoformat'], ISO8601_FORMAT)
        hour = datetime.datetime.strftime(time,'%Y-%m-%d %H')
        minute = datetime.strptime(time,'%Y-%m-%d %H:%M')
        if minute in mins:
            mins[minute] += 1
        else:
            mins[minute] = 1

    return mins




