#!/usr/bin/python
#Program to run OWASP ZAP scan using ZAP Docker
#Desinged by Saqib Ahmed Warsi

import os
import subprocess
import sys
import datetime
import time
start = time.time()


fileexists = os.path.isfile('/tmp/output.log')
if fileexists:
   os.remove("/tmp/output.log")
else:
    print ""

fileexists = os.path.isfile('/tmp/grp-output.log')
if fileexists:
    os.remove("/tmp/grp-output.log")
else:
    print ""

#Calling subprocess call for docker run
datetime = datetime.datetime.now()
random = datetime.strftime("%I%M%S")
uri_to_scan = raw_input('Please enter uri to scan: ')
grpcmd1 = "echo "
grpcmd2 = (uri_to_scan)
with open("/tmp/grp-output.log", "a") as output:
     subprocess.call(grpcmd1+grpcmd2, shell=True, stdout=output, stderr=output)

fileexists = os.path.isfile('/tmp/url-output.log')
if fileexists:
   os.remove("/tmp/url-output.log")
else:
    print ""

repcmd1 = "cat /tmp/grp-output.log"
repcmd2 = " | tr ':' ' '| tr '/' ' '"
repcmd3 = " | awk '{print $2}'"
with open("/tmp/url-output.log", "a") as output:
     subprocess.call(repcmd1+repcmd2+repcmd3, shell=True, stdout=output, stderr=output)

with open("/tmp/url-output.log", 'r') as file:
    url = file.read()

cmd1 = "docker run -v /tmp:/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t " 
cmd2 = (uri_to_scan).rstrip('\r\n')
cmd3 = " -r Report-" + (random)+ '-' + url.rstrip('\r\n') + ".html"      
# Note: rstrip is used to remove \n (carriage return for this variable

with open("/tmp/output.log", "a") as output:
    subprocess.call(cmd1+cmd2+cmd3, shell=True, stdout=output, stderr=output)

#Printing Report location and name
print "Report generated at /tmp folder"
print ("+++++++++++++++++++++++++++++++++++++++++")
report_name = "Report-" + (random) + '-' + (url)
print "Report Name:", report_name
print ("+++++++++++++++++++++++++++++++++++++++++")

#Calculation for the elapsed time to generate Html report
end = time.time()
elapsed = (end - start)/60
print "Time to generate this report", elapsed
