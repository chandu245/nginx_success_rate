import re

logformat = re.compile(r""" (?P<statuscode>\d{3}) """, re.IGNORECASE)
logfile = open("logs.txt", "r")
count=0
success=0
for line in logfile.readlines():
    search = re.search(logformat, line)
    if search:
            searchdict = search.groupdict()
            status = searchdict["statuscode"]
            count=count+1
            if (status.find('200') and status.find('304')) == 0:
                success= success + 1
successrate = success/count * 100
print (f'Success rate for current log file is {successrate:.2f} %')
logfile.close()
