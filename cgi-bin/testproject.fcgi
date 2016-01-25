#!/usr/bin/python
import sys, os

basepath = 'nuclearpowerplantconference.com/kunden/homepages/13/d609847479/htdocs'

sys.path.insert(0, basepath + '/.local/lib')
sys.path.insert(0, basepath + '/www/testproject')

os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method='threaded', daemonize='false')