#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import base64
import xml.etree.ElementTree as ET

if len(sys.argv) < 2:
	print('Not enough actual parameters')
	sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]

tree = ET.parse(inputFile)
root = tree.getroot()

cover_raw = None

for i in root.iter():
	if (i.tag.split('}')[1] == 'binary') and ('id' in i.attrib) and (i.attrib['id'].split('.')[0] == 'cover'):
		cover_raw = i.text
		open(outputFile,'wb').write(base64.decodestring(cover_raw))
		sys.exit(0)

print('No cover inside')
sys.exit(2)
