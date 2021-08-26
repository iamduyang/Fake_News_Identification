#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import xlwt
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
	
	
	
if __name__ == '__main__':	
	#analyzeFile('1.txt')
	wb = xlwt.Workbook()
	ws = wb.add_sheet('A Test Sheet')
	cont=range(1,74)
	for x in cont:
		filePath1=str(x)+'.txt'
		analyzeFile(filePath1,ws,x)

	wb.save('example5.xls')