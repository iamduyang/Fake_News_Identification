#!/usr/bin/python
# -*- coding:utf8 -*-
import os
import Image  

items = os.listdir(".")
items[5].decode('gbk')
#gifCont = 0
#newlist = []

# for names in items:
	# if names.endswith(".gif"):
		#newlist.append(names)
		# jpgName = names[0:len(names)-3]
		# jpgName = jpgName+'jpg'
		# gifCont = gifCont +1 
		# im = Image.open(names)    
		# im = im.convert('RGB')                  
		# im.save(jpgName,"jpeg")    #保存图像为jpeg格式
		# os.remove(names)
		
# print "gifCont:  ",gifCont