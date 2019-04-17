# Web Application Scanning

Scanning a web application is an important part of internal security of any organization. There are different Web application scanner available, including free and paid but there is no standard scanner. But if it comes to the standardization of severity of web application vulnerabilities, OWASP (Open Wep Application Security Project) is REALLY on top of the list. 

OWASP top 10, updated in Nov 2017, defines top 10 vulnerabilities in web application:

https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf

OWASP provided a scanner to detect these top 10 vulnerabilities and identifies them as High, Medium and Low. OWASP scanner is named as ZAP (Zed Attack Proxy) scanner. Here is the link for it: 

https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project

You can install OWASP ZAP in different platform including Kali Linux. You can scan web application using GUI but in order to automate and run it from command line, you need some scripts. I wrote some python scripts to scan a web application:

scan_single.py    -       This script will scan a single URL
scan_group.py     -       This script will scan a list of URLs in a text file

Note: You need to download and install docker for OWASP ZAP from:

https://github.com/zaproxy/zaproxy/wiki/Docker

https://github.com/zaproxy/zaproxy/wiki/ZAP-Baseline-Scan

