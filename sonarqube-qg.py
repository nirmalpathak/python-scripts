#!/usr/bin/env python

import os, sys, json, requests

arg = sys.argv[1]

def get_status(status):
        staturl = "https://sonar.domain.net/api/ce/activity?status=IN_PROGRESS&q=com.domain:"+arg
        response = requests.get(staturl, auth=(os.environ['SONAR_USERNAME'], os.environ['SONAR_PASSWORD']))
        data = response.json()
        t = data['tasks']
        return len(t)

def get_qg(proj):
        qgurl = "https://sonar.domain.net/api/qualitygates/project_status?projectKey=com.domain:"+proj
        qgresp = requests.get(qgurl, auth=(os.environ['SONAR_USERNAME'], os.environ['SONAR_PASSWORD']))
        qg = qgresp.json()
        return qg['projectStatus']['status']

t = get_status(arg)
print t
if t != 0:
        print ("SonarQube Background Task is in progress!")
        while t != 0:
                #print ("Background Task is in progress!")
                t = get_status(arg)
                #print t

        qgstatus = get_qg(arg)
        print qgstatus
        if qgstatus == 'OK':
                print '\033[1;32mQuality Gate PASSED!\033[1;m'
                sys.exit(0)
        else:
                print '\033[1;31mQuality Gate FAILED!\033[1;m'
                sys.exit(127)
else:
        qgstatus = get_qg(arg)
        print qgstatus
        print ("SonarQube Background Task is not in progress!")
        if qgstatus == 'OK':
                print '\033[1;32mQuality Gate PASSED!\033[1;m'
                sys.exit(0)
        else:
                print '\033[1;31mQuality Gate FAILED!\033[1;m'
                sys.exit(127)
