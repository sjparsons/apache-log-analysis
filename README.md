# Apache log analysis

This is a package of utility scripts for parsing and reporting on apache logs. 
It uses the Rory's [Apache Log Parser](https://github.com/rory/apache-log-parser) 
under the hood and builds on it with some utility functions to make it quick to 
get the answers your looking for. 

The idea is that this repository provides an environment to build your own 
recipes for getting the information **you** need, but gives you examples to 
get started and some of the most common recipes. 


**Note:** Currently there is little in the way of seatbelts, parachutes or that type of thing. In other words, this scripts might fail in unexpected ways if not used appropriately.

## 1. Process logs
    
This script takes a raw apache log and outputs a processed JSON array of 
objects each one representing a single log entry. The advantage is that on 
large log files, processing the logs takes a long time, and it's more efficient
to only do that step once, and then build reports on that processed data.

    $ python parse.py <raw-file> <processed-file> <format>

* `<raw-file>` – the original apache log file
* `<processed-file>` – the location to output the processed JSON
* `<format>` – An apache log format. 


**Log formats**

* `APACHE_COMMON`, for example:  
  ```
  %h %l %u %t \"%r\" %>s %b
  ```
* `APACHE_SSL`, for example:  
  ```
  %t %h %l %k \"%r\" %b
  ```
* `APACHE_COMBINED`, for example:  
  ```
  %h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"
  ```
* `APACHE_COMBINED_IO`, for example:  
  ```
  %h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O
  ```
* `APACHE_COMBINED_PIPE`, for example:  
  ```
  %P¦¦%h¦¦%l¦¦%u¦¦%t¦¦\"%r\"¦¦%>s¦¦%b¦¦\"%{Referer}i\"¦¦\"%{User-Agent}i\"
  ```

Implementation note: JSON is obviously not the most compact intermediate format
to store processed data in. During development, I investigated both cPickle and 
[MessagePack](http://msgpack.org/index.html), but JSON has the advantage of 
being both human readable (and editable) and easily accessible in most
languages should you wish to do something else with the processed data.

## 2. Reduce logs

Sometimes you want to reduce logs to only focus on logs in a certain time 
period or to a certain URL, or on some other metric. Here are some starter
reducing scripts.

### Limit by URL

Create a reduced log file with request URL's that match the given regular
expression.

    $ python limitUrl.py <processed-in> <processed-out> <url-regex>

* `<processed-in>` – a processed log file
* `<processed-out>` - the location to output the reduced log file
* `<url-regex>` - a regex to use to match URL's


## 3. Reports

After processing (and possibly reducing) the logs into a JSON file, you can 
take advantage of the following pre-built report scripts. You can use the 
scripts as is, but you can also duplicate, extend and modify modify to your 
meet your needs. 

### Paths visited

Report the aggregated number of visits to requested URL paths, to the given depth.

    $ python paths.py <processed-data-file> <depth>

* `<processed-file>` – processed file to report on
* `<depth>` – depth of path. Literally "how many slashes in the request".

### Hours

Report the number of visits on a per day and hour across the time period in the
processed log.

    $ python hours.py <processed-data-file>

* `<processed-file>` – processed file to report on

### Hours totals

Report the number of visits hour totalled across the time period in the
processed log.

    $ python hoursTotals.py <processed-data-file>

* `<processed-file>` – processed file to report on

### Referers

Report the aggregated number of requests with given referers

    $ python referers.py <processed-data-file>

* `<processed-file>` – processed file to report on


## Contributions

Contributions are welcome; please submit a pull request!


## Copyright and license 

Apache Log Parser is © 2013 Rory McCann and released GNU GPL v3.

All other code is released under the GNU GPL v3.