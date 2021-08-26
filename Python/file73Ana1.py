#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import xlwt
import os

def analyzeFile(fileName,ws,x):	
	f = open(fileName, "r")  
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
	ws.write(x-1, 0, httpCont)
	ws.write(x-1, 1, imageCont)
	ws.write(x-1, 2, imageCont)
	ws.write(x-1, 3, atCont)
	ws.write(x-1,4,os.path.getsize(fileName))
	
	
	
if __name__ == '__main__':	
	#analyzeFile('1.txt')
	wb = xlwt.Workbook()
	ws = wb.add_sheet('A Test Sheet')

	#ws.write(0, 0, 1234.56)
	#ws.write(1, 0, 555)
	#ws.write(2, 0, 1)
	#ws.write(2, 1, 1)
	analyzeFile('1.txt',ws,1)

	wb.save('exampleSize.xls')