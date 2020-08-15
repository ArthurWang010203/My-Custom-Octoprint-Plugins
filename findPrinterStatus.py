from __future__ import absolute_import, unicode_literals
from datetime import datetime
import datetime
import time
import socket
import os

import octoprint.plugin
import octoprint.util
import traceback
from octoprint.events import Events

class GetStatus(octoprint.plugin.EventHandlerPlugin, octoprint.plugin.SettingsPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin, octoprint.plugin.StartupPlugin):
	def on_event(self,event,payload):
		currentStatus = ""
		startTime = ""
		if event == Events.PRINT_STARTED:
			currentStatus = "Printing..."
			#startTime = datetime.now()
                        #startTime = startTime.strftime("%m/%d/%Y, %H:%M:%S")
		elif event == Events.PRINT_FAILED:
			currentStatus = "Available (Last Print Cancelled/Failed)"
			#startTime = ""
		elif event == Events.PRINT_DONE:
			currentStatus = "Available (Last Print Finished)"
			#startTime = ""
		elif event == Events.PRINT_PAUSED:
			currentStatus = "Print Paused"
		elif event == Events.PRINT_RESUMED:
			currentStatus = "Printing..."
		elif event == Events.ERROR:
			currentStatus = "Error!"
		elif event == Events.CONNECTED:
			currentStatus = "Connected"
		elif event == Events.DISCONNECTED:
			currentStatus = "Disconnected"
		#elif event != Events.PRINTER_STATE_CHANGED:
			#currentStatus = "Available"
		#self._logger.info("Event= "+event+" - currentStatus= "+currentStatus) #for testing event triggers
		if currentStatus != "":
			printerName = ""
			f = open('home/pi/OctoPrint/status.txt','w') #open output file
			file1 = open('/home/pi/.octoprint/printerProfiles/_default.profile', 'r') #open _data.profile file which contains printer profile name
			Lines = file1.readlines()
			connectionInfo = os.system("hostname -I | cut -f1 -d' ' > home/pi/") #str(os.system('hostname -I')).split(" ")
			for line in Lines:
        			tempLine = line.split(':') #the line we want in _data.profile starts with 'model': printer_name
        			if(tempLine[0]=='model'):
                			printerName = tempLine[1][1:] #remove space in front of printer_name
			#job = self._printer.get_current_data()["job".encode("utf-8")]
			#secondsJob = float(job['estimatedPrintTime'])
			#printTime = str(datetime.timedelta(seconds=secondsJob))
			f.write(printerName)
			#self._logger.info(str(connectionInfo).encode("utf-8") + "-------------------------------------------------------------------------------------------------")
			f.write(currentStatus)
			#f.write("\n")
			#f.write(connectionInfo)
			#f.write(startTime)
			#f.write("\n")
			#f.write(printTime)
			f.close()

__plugin_implementation__ = GetStatus()
