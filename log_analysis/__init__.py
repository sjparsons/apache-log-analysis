

import apache_log_parser
import glob  
import sys  
import json, calendar, datetime




class LogFormats:
    _PIPE="\xc2\xa6\xc2\xa6"

    # Log formats
    APACHE_COMMON="%h %l %u %t \"%r\" %>s %b"
    APACHE_SSL="%t %h %l %k \"%r\" %b"
    APACHE_COMBINED="%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""
    APACHE_COMBINED_IO="%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O"
    APACHE_COMBINED_PIPE="%P"+_PIPE+"%h"+_PIPE+"%l"+_PIPE+"%u"+_PIPE+"%t"+_PIPE+"\"%r\""+_PIPE+"%>s"+_PIPE+"%b"+_PIPE+"\"%{Referer}i\""+_PIPE+"\"%{User-Agent}i\""


def parse(log_file_path, log_format=LogFormats.APACHE_COMBINED):  
    """ import and parse log files using the apache log parser """
    log_data = []
    line_parser = apache_log_parser.make_parser(log_format)  
    
    for file_name in glob.glob(log_file_path):  
        sys.stdout.write("\nFile name: %s\n" % file_name)  
     
        with open(file_name,'r') as f:
            for i, l in enumerate(f):
                pass
            total = i + 1
            f.seek(0)
            for counter, line in enumerate(f):
                percent = 100.0 * (counter+1) / total
                log_data.append( line_parser(line) )
                sys.stdout.write("\rProcessed %i of %i entries (%i%%)" % (counter, total, percent ))
                sys.stdout.flush()

    sys.stdout.write("\n")    
    return log_data  



def json_serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")


def save(log_data, filename):
    with open(filename, 'wb') as f:
        json.dump(log_data, f, default=json_serialize)

def load(filename):
    with open(filename,'rb') as f:
        data = json.load(f)
    return data

