#!/usr/bin/python
# -*- coding:utf8 -*-
import os
import Image  
for x in range(1,74):
	os.chdir('../'+str(x))
	items = os.listdir(".")
	jpgCont = 0
	newlist = []
	for names in items:
		if names.endswith(".jpg"):

			jpgCont = jpgCont +1 
		
			
	print jpgCont