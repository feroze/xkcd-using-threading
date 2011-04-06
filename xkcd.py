#!/usr/bin/env python

'''
Uses threading to make multiple instances
I/O is the bottleneck

TODO : Should use urllib3 for port reuse

Feroze Naina
'''

import urllib2
from BeautifulSoup3 import BeautifulSoup
from threading import Thread
import os

if not os.path.isdir('comics'):
    os.mkdir('comics')
    


os.chdir("./comics/")

def myfunc(i):
    for i in range(i,i+10):
        if (i != 404) and (i !=472): #404 doesnt work and 472 has stupid css tags causing errors
            response = urllib2.urlopen("http://xkcd.com/"+str(i)+"/")
            page=response.read()
                        
            soup=BeautifulSoup(page)
            results = soup.findAll('img')
            picture_page = results[1]['src']
            
            opener1 = urllib2.build_opener()
            page1 = opener1.open(picture_page)
            my_picture = page1.read()
            
            filename = str(i) + ' - ' + results[1]['alt']
            fout = open(filename, "wb")
            fout.write(my_picture)
            fout.close()
            print "Writing to " + filename
            
            
        

for i in range(1,861,10):
    t = Thread(target=myfunc, args=(i,))
    t.start()

