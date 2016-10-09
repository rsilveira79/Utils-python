#!/usr/bin/python

import urllib2
from time import sleep
import csv
import time

def check_internet():
    try:
        header = {"pragma" : "no-cache"} # Tells the server to send fresh copy
        req = urllib2.Request("http://www.google.com", headers=header)
        response=urllib2.urlopen(req,timeout=2)
        print "You are connected !"
    except urllib2.URLError as err:
        print "Connection lost!"
        writer.writerow([time.ctime(), str(err)])
        return err

if __name__ == "__main__":
    row = [time.ctime()]
    dataCSV = open('internetlog.csv', 'a')
    writer=csv.writer(dataCSV,dialect='excel',delimiter=',')
    writer.writerow(['Time Stamp','Error'])
    while True:
        test=check_internet()
        sleep(5)
