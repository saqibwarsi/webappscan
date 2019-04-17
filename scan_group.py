#Program to run OWASP ZAP scan using ZAP Docker
#Desinged by Saqib Ahmed Warsi
#!/usr/bin/python
import os
import subprocess
import sys
import datetime
import time
import random

start = time.time()
fileexists = os.path.isfile('/tmp/output.log')
if fileexists:
   os.remove("/tmp/output.log")
else:
    print ""

datetime = datetime.datetime.now()
random_number = datetime.strftime("%I%M%S")
name_of_uri_file = raw_input('Enter the name of file with all URIs to scan: ')

cmd = 'pwd'
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
loc = out.rstrip('\r\n') 
loc = loc + '/' + name_of_uri_file 

cmd = 'touch /tmp/Report-' + name_of_uri_file + "-" + random_number + ".html"
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

rpt_name = 'Report-' + name_of_uri_file + "-" + random_number + ".html"

count = 0
with open(loc) as f:
     for line in f:
         count+=1
         rannumb = random.randint(1,2000000)

         repcmd1 = "echo " + line.rstrip('\r\n')
         repcmd2 = " | tr ':' ' '| tr '/' '*'"
         repcmd3 = " | awk '{print $2}'"
         proc = subprocess.Popen(repcmd1+repcmd2+repcmd3, stdout=subprocess.PIPE, shell=True)
         (out, err) = proc.communicate()
         url = out
         
         cmd1 = "docker run -v /tmp:/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t "
         cmd2 = line.rstrip('\r\n') + " -r " 
         indv_report_name = 'Report-' + url.rstrip('\r\n') + '-' + str(rannumb) + '.html'
         with open("/tmp/output.log", "a") as output:
              subprocess.call(cmd1+cmd2+indv_report_name, shell=True, stdout=output, stderr=output)
         
         cmd = 'cat /tmp/' + indv_report_name.rstrip('\r\n') + ' >> ' + '/tmp/' + rpt_name 
         proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
         (out, err) = proc.communicate()
         
#Printing Report location and name
print "Report generated at /tmp folder"
print ("+++++++++++++++++++++++++++++++++++++++++")
print "Final Report Name:", rpt_name
print ("+++++++++++++++++++++++++++++++++++++++++")

#Calculation for the elapsed time to generate Html report
end = time.time()
elapsed = (end - start)/60
print "Time to generate this report", elapsed
