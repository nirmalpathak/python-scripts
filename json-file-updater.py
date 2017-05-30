#!/usr/bin/env python
#############################################################
# # Author:   Nirmal Pathak
# License: GPLv2 (https://www.gnu.org/licenses/gpl-2.0.txt)
# Web:      
#
# Program:
#   Script to update JSON file variables. 
#
############################################################

import json
import os

f = open("/tmp/bo-mup.json", 'r')
data = json.load(f)
data['appName'] = 'myapp-'+os.environ["BO_PORT"]
data['app'] = os.environ["WORKSPACE"]+'/myapp'
data['env']['PORT'] = os.environ["BO_PORT"]
data['env']['SITE_URL'] = 'http://example.com:'+os.environ["PUBLIC_PORT"]
dump = json.dumps(data, indent=4) # 2 = '\t', 4 = '\t\t', etc
f.close()
print (dump)
