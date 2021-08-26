#!/usr/bin/python
# -*- coding:utf8 -*-

import os

def getDirList( p ):
        p = str( p )
		#c=[]
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
             p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isdir( p + x ) ]
		#for y in b:
		#	pass
			
        return b

a = getDirList( '.\\' )	
cont =1 
for x in a:
	split1 = os.path.split(x)
	print x
	os.rename(x,split1[0]+"\\"+str(cont))
	cont = cont +1
	print '\n'

#print   a