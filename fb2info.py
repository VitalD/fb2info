#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import base64
import xml.etree.ElementTree as ET
import Image
from StringIO import StringIO

if len(sys.argv) < 3:
	print('Not enough actual parameters')
	sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]
size = int(sys.argv[3])

root = ET.parse(inputFile).getroot()

for i in root.iter():
	if (i.tag.split('}')[1] == 'binary') and ('id' in i.attrib) and (i.attrib['id'].split('.')[0] == 'cover'):
		cover_raw = i.text
		cover_decoded = base64.decodestring(cover_raw)
		cover = Image.open(StringIO(cover_decoded))
		cover.thumbnail((size,size), Image.ANTIALIAS)
		cover.save(outputFile,"PNG")
		sys.exit(0)

print('No cover inside')
sys.exit(2)
