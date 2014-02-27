#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import base64
import xml.etree.ElementTree as ET
import Image
from StringIO import StringIO
import urllib

if len(sys.argv) < 2:
	print('Not enough actual parameters')
	sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]
if len(sys.argv) > 2:
	size = int(sys.argv[3])
else:
	size = 256

iFile = open(urllib.url2pathname(inputFile).split('file://')[1],'r')
root = ET.parse(iFile).getroot()

def saveCover(cover_raw):
	cover_decoded = base64.decodestring(cover_raw)
	cover = Image.open(StringIO(cover_decoded))
	cover.thumbnail((size,size), Image.ANTIALIAS)
	cover.save(outputFile,"PNG")
	sys.exit(0)

for i in root.iter():
	if (i.tag.split('}')[1] == 'binary') and ('id' in i.attrib) and (i.attrib['id'].split('.')[0] == 'cover'):
		saveCover(i.text)

for i in root.iter():
	if (i.tag.split('}')[1] == 'binary') and ('content-type' in i.attrib) and (i.attrib['content-type'].split('/')[0] == 'image'):
		saveCover(i.text)

print('No cover inside')
sys.exit(2)
