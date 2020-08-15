from __future__ import absolute_import, unicode_literals
from datetime import datetime
import time
import socket
import os
import sys

import octoprint.plugin
import octoprint.util
import traceback
from octoprint.events import Events

class TrackPrintResult(octoprint.plugin.EventHandlerPlugin, octoprint.plugin.SettingsPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin, octoprint.plugin.StartupPlugin):
	def on_event(self,event,payload):
		if event == Events.PRINT_STARTED:
			self._logger.info("Print Job Started with Python version: "+sys.version)
			#self._logger.info(sys.version)
			#Print Started custom notification

			#job = self._printer.get_current_data()["job".encode("utf-8")]
			#Get the job object, which contains data about the current job 
			# (see /home/pi/oprint/lib/python2.7/site-packages/octoprint/printer/standard.py 's get_current_data() function)

			#self._logger.info(job)
			#log current job information

			#user = job['user']
			#get the username of the person who started this job

			#self._logger.info("user: " + user)
			#log username

			#file = job['file']
			#get file dictionary (contains more information on job)

			#name = file['name']
			#get file/job name

			#self._logger.info("file.name: " + name)
			#log job name

		elif event == Events.PRINT_CANCELLED:
			job = self._printer.get_current_data()["job".encode("utf-8")]
			#get current job data
			#self._logger.info(job)
			#self._logger.info("^^^^^^^^^^^^^^^^^^^")
			currentDT = datetime.now()
			currentDT = currentDT.strftime("%m/%d/%Y, %H:%M:%S")
			outputString = ("\n"+currentDT+" - "+job['file']['name']+" - Started by: "+job['user']+" - End Result: Print Cancelled\n")
			f = open('home/pi/printData.txt','a')
			f.write(outputString)
			f.close()
		elif event == Events.PRINT_DONE:
			job = self._printer.get_current_data()["job".encode("utf-8")]
			#secondsJob = round(float(job['estimatedPrintTime']),2)
			#printTime = str(datetime.timedelta(seconds=secondsJob))
			#job = {'averagePrintTime': None, 'lastPrintTime': None, 'user': 'jabbawithlegs', 'file': {'origin': u'local', 'name': u'CE3_Front_03Engines_02.gcode', 'date': 1593612385, 'path': u'CE3_Front_03Engines_02.gcode', 'display': u'CE3_Front_03Engines_02.gcode', 'size': 2031659L}, 'estimatedPrintTime': 1922.81619726344, 'filament': {u'tool0': {u'volume': 0.0, u'length': 1491.1642299999985}}}
			currentTime = datetime.now()
			currentTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
			#printTime = str(datetime.timedelta(seconds=secondsJob))
			outputString = ("\n"+currentTime+" - "+job['file']['name']+" - Started by: "+job['user']+" - End Result: Print Finished\n")
			f = open('home/pi/printData.txt','a')
			f.write(outputString)
			f.close()
__plugin_implementation__ = TrackPrintResult()

