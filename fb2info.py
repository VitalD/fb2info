#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import getopt,sys,base64,os
try:
	optlist, args = getopt.getopt(sys.argv[1:],'',[''])
except getopt.GetoptError:
	print('Error in parameters')
	sys.exit(1)
if len(args)!=3:
	print('Not enough actual parameters')
	sys.exit(2)
cover_raw=[etree.parse(args[0]).findtext('{http://www.gribuser.ru/xml/fictionbook/2.0}binary')]
if cover_raw!=None:
	open(args[1],'wb').write(base64.decodestring(''.join(cover_raw)))
	sys.exit(0)
else:
	print('No cover inside')
	sys.exit(3)
