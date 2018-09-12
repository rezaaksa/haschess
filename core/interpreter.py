#!/usr/bin/env python
#-*-coding:utf-8-*-
# (C) Copyright 2018 LOoLzeC Scurity
# Date : 14 maret 2018
# Hasches framework By Deray
# Contact instagram @reyy05_
import os, sys, urllib, json
from time import *
from tools.colors.colors import *
from tools.md5 import *
from tools.sha1 import *
from tools.sha224 import *
from tools.sha256 import *
from tools.sha384 import *
from tools.sha512 import *
from tools.options.interpreter_options import *
hes = " "
def m():
	print 
	print "%sMODULES\n======%s\n"%(WHITEBOLD,RED)
	print "\t%sName\t\t\t\tDescription\n\t%s----\t\t\t\t----------"%(WHITEBOLD,RED)
	print "\tgenerate/password/type/md5\tgenerate password type md5"
	print "\tgenerate/password/type/sha1\tgenerate password type sha1"
	print "\tgenerate/password/type/sha224\tgenerate password type sha224"
	print "\tgenerate/password/type/sha256\tgenerate password type sha256"
	print "\tgenerate/password/type/sha384\tgenerate password type sha384"
	print "\tgenerate/password/type/512\tgenerate password type sha512"
	print "\thash <STRING>\t\t\te.g hash 35be991f550bbaa1be9f6ca503c"
	print 
# Running
def main():
	while True:
		try:
			hasches=raw_input("%s%shasches%s%s> "%(WHITEBOLD,LINE,STOPLINE,WHITEBOLD))
			if "generate/password/type/md5" in hasches:
				md5()
			elif "generate/password/type/sha1" in hasches:
				shaone()
			elif "generate/password/type/sha224" in hasches:
				sha224()
			elif "generate/password/type/sha256" in hasches:
				sha256()
			elif "generate/password/type/sha384" in hasches:
				sha384()
			elif "generate/password/type/sha512" in hasches:
				sha512()
			elif "show modules" in hasches:
				m()
			elif "clear" in hasches:
				os.system("clear")
			elif "exit" in hasches:
				sys.exit()
			elif hasches == 'show options' or hasches == '?' or hasches == 'help':
				iop()
			elif "hash" in hasches:
				hes=hasches.split()[-1]
				print "STRING => ",hasches.split()[-1]
				print "%s[*]%s Cracking.."%(BLUE,WHITEBOLD)
				try:
					url = "https://lea.kz/api/hash/%s"%(hes)
					beheading = urllib.urlopen(url).read()
					data = json.loads(beheading)
					print "%s[+]%s STRING : %s"%(BLUE,WHITEBOLD,hes)
					print "%s[*]%s RESULT : %s%s"%(RED,WHITEBOLD,RED,data["password"])
				except:
					print "%s[!]%s STRING NOT FOUND!"%(RED,WHITEBOLD)
			else:
				print "%s[-] Unknown command : %s%s%s"%(RED,WHITEBOLD,hasches,RED)
				print "[!] U can enter 'help' ?"
		except:
			print "\nBye"
			sys.exit()
