
#menu.py
import time
import kbhit
import os
import sys 
import signal 
import subprocess

signal.signal(signal.SIGINT, signal_handler)
def signal_handler(signal,frame):
	kbhit.restore_stdin()
	print "Caught SIGINT            "	
	print "Restoring stdin"
	kbhit.restore_stdin()
	exit(0)
	
def restore_stdin():
	kbhit.restore_stdin()
def unbuffer_stdin():
	kbhit.unbuffer_stdin()
def banner():
	print "*" * 80
	print " " * 35+"Welcome to"
	print "*" * 80
	print " " * 12 +"   ___  _   _   _    ____   ____    _    ____  _____"
	print " " * 12 +"  / _ \| | | | / \  |  _ \ / ___|  / \  |  _ \| ____|"
	print " " * 12 +" | | | | | | |/ _ \ | | | | |     / _ \ | |_) |  _|  "
	print " " * 12 +" | |_| | |_| / ___ \| |_| | |___ / ___ \|  __/| |___ "
	print " " * 12 +"  \__\_\\___/_/   \_\____/ \____/_/   \_\_|   |_____|"
	print "*" * 80
	print " " * 32 + "Raising innovation"
	print "*" * 80
	return
def print_menu(title, lines):
	LINE_LENGTH=48
	print "\n"+" " *10 + "*"*60+"\n"+" "*10+"*"+" "*26+title+" "*25+"*\n"+" " *10 + "*"*60+"\n"+" "*10+"*"+" "*58+"*\n",
	for line in lines:
		print " " *10+"*    ",
		if len(line)<LINE_LENGTH:
			print line,
		else:
			print line[0:LINE_LENGTH],
		print " "* (LINE_LENGTH-len(line))+"    *"
	print " "*10+"*"+" "*58+"*\n"+" " *10 + "*"*60+"\n"
	return
	
	
class submenu:
	CLEAR_ON_REFRESH=1
	PRINT_ON_REFRESH=1
	IDLE_FUNCTION=0
	
	def __init__(self,title_in,items_in,functions_in,keys_in):
		self.title=title_in
		self.items=items_in
		self.functions=functions_in
		self.keys=keys_in
		for x in range(0,len(self.keys)):
			self.keys[x]=self.keys[x].lower()
	def display(self):
		noresponse=1
		self.refresh(1)
		while noresponse==1:
			if IDLE_FUNCTION!=0:
				IDLE_FUNCTION()
			if kbhit.kbhit()>0:
					char=kbhit.getch().lower()	
					for x in range(0,len(self.keys)):
						if char==self.keys[x]:
							self.functions[x]()
							noresponse=0
			self.refresh()
	def refresh(self,force=0):
		if force==1:
			try:
				subprocess.call(["clear"])
			except OSError:
				subprocess.call(["cls"])
			finally:	
				print_menu(self.title,self.items)
			return

		if CLEAR_ON_REFRESH==1:
			try:
				subprocess.call(["clear"])
			except OSError:
				subprocess.call(["cls"])
		if PRINT_ON_REFRESH==1:
			print_menu(self.title,self.items)
		return
		