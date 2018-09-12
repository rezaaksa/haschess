#!/usr/bin/env python
#-*-coding:utf-8-*-
# (C) Copyright 2018 LOoLzeC Scurity
# Date : 14 maret 2018
# Hasches framework By Deray
# Contact instagram @reyy05_
import os
import urllib
import json
import sys
from colors.colors import *
md = " "

# Back
def rest():
	os.system("clear")
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
# Settings
def options():
	print "\n%sOPTIONS\n%s=======%s"%(WHITEBOLD,RED,WHITEBOLD)
	print 
	print "\tName\t\tDescription\t\tRequired?%s"%(RED)
	print "\t----\t\t----------\t\t--------"
	print "\tset string\tSTRING\t\t\tyes"
	print "\trun\t\tstart cracking\t\tyes"
	print "\tclear\t\tclear screen\t\tN/A"
	print "\tshow options\tsettings\t\tyes"
	print "\tback\t\tback"
	print "\texit\t\tbye"
	print 
	print "%sCurrent settings\n%s-----------------%s"%(WHITEBOLD,RED,WHITEBOLD)
	print "%s\n\n"%(md)
# Running
def md5():
	global md
	while True:
		try:
			mdfive=raw_input("%s%shasches%s%s> generate%s(MD5)%s> "%(WHITEBOLD,LINE,STOPLINE,WHITEBOLD,RED,WHITEBOLD))
			if "set string" in mdfive:
				md=mdfive.split()[-1]
				print "STRING => ",mdfive.split()[-1]
			elif "clear" in mdfive:
				os.system("clear")
			elif "exit" in mdfive:
				exit()
			elif "back" in mdfive:
				rest()
			elif mdfive == 'show options' or mdfive == '?' or mdfive == 'help':
				options()
			elif mdfive == 'run' or mdfive == 'start':
				print "%s[*]%s Cracking..."%(BLUE,WHITEBOLD)
				try:
					url = "https://lea.kz/api/password/%s"%(md)
					head = urllib.urlopen(url).read()
					data = json.loads(head)
					print "%s[+]%s STRING : %s"%(BLUE,WHITEBOLD,md)
					print "%s[*]%s RESULT : %s%s"%(RED,WHITEBOLD,RED,data["md5"])
				except:
					print "%s[!]%s STRING NOT FOUND!"%(RED,WHITEBOLD)
				
			else:
				print "%s[-] Failed to load command : %s%s"%(RED,WHITEBOLD,mdfive)
		except:
			sys.exit()
