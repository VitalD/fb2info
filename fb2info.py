#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import getopt
import sys
import base64
import os

ns='{http://www.gribuser.ru/xml/fictionbook/2.0}'
try:
	optlist, args = getopt.getopt(sys.argv[1:],'',[''])
except getopt.GetoptError:
	sys.exit(1)
if len(args)!=3:
	sys.exit(1)
filename=args[0]
outputfile=args[1]
size=args[2]
doc = etree.parse(filename)
cover_raw=[doc.findtext(ns+'binary')]
if not cover_raw==None:
	cover=base64.decodestring(''.join(cover_raw))
	open(outputfile,'wb').write(cover)
	sys.exit(0)
else:
	sys.exit(1)
