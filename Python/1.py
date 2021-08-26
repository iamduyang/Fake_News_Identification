#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

if __name__ == '__main__':	
	f = open("1.txt", "r")  
	httpCont = 0 
	imageCont = 0
	atCont = 0
	weiboCont = 1 # null的个数+1=微博的个数
	while True:  
		line = f.readline()  
		if line:    
			#print line.count('http')
			#httpCont = cont+line.count('http')
			httpCont = httpCont+line.count('http')
			imageCont = imageCont+line.count('jpg')+line.count('gif')
			atCont = httpCont+line.count('@')
			weiboCont = httpCont+line.count('null')
		else:  
			break
	f.close()  
	print "httpCont   "+str(httpCont)+"\n"+"imageCont   "+str(imageCont)+"\n"+"atCont   "+str(atCont)+"\n"+"weiboCont   "+str(weiboCont)+"\n"