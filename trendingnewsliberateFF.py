
# coding: utf-8

# In[1]:




import bs4 as bs
import urllib2
from urllib2 import urlopen
import datetime
#import pandas as pd
#import csv
#import json
from pymongo import MongoClient

conn = MongoClient("localhost", 27017)
conn = MongoClient()
db=conn.tryThree
collection = db.cThree



arr=[]

entry=input('The topic on which news you want to find:')
print(entry)



#BBC START
e=entry.split(" ")
#print(e)
fin='+'.join(e)

source=['https://www.bbc.co.uk/search?q='+fin+'&sa_f=search-product&scope=#page=15']


#print("----------BBC NEWS----------")
for n in range(0,1):
    page=urllib2.urlopen('https://www.bbc.co.uk/search?q='+fin+'&sa_f=search-product&scope=#page=15').read()
    soup=bs.BeautifulSoup(page,'lxml')
    for i in soup.find_all('section',{'class':'search-content'}):
        for j in i.find_all('ol',{'class':'search-results results'}):
            for k in j.find_all('article',{'class':'has_image media-video'}):
                #print("**********")
                dict={}
                for l in k.find_all('div'):
                    for n in l.find_all('a'):
                        dict['headlines']=n.text
                        dict['link']=n.get('href')
                        
                for m in k.find_all('aside',{'class':'flags top'}):
                    for l in m.find_all('dd'):
                        f=l.text
                        d=str(datetime.datetime.strptime(f,'\n\n           %d %b %Y       \n'))
                        dict['date']=d
                        
                for o in k.find_all('div'):
                    for p in o.find_all('p',{'class':'summary medium'}):
                        dict['descrip']= p.text
                arr.append(dict)
                collection.insert_one(dict)
            
                    
            for k in j.find_all('article',{'class':'has_image media-text'}):
                #print("**********")
                dict={}
                for l in k.find_all('div'):
                    for n in l.find_all('a'):
                        dict['headlines']=n.text
                        dict['link']=n.get('href')
                        
                for m in k.find_all('aside',{'class':'flags top'}):
                    for l in m.find_all('dd'):
                        f=l.text
                        d=str(datetime.datetime.strptime(f,'\n\n           %d %b %Y       \n'))
                        dict['date']=d
                        
                for o in k.find_all('div'):
                    for p in o.find_all('p',{'class':'summary medium'}):
                        dict['descrip']= p.text
                arr.append(dict)
                collection.insert_one(dict)
            for k in j.find_all('article',{'class':'has_image media-audio'}):
                #print("**********")
                dict={}
                for l in k.find_all('div'):
                    for n in l.find_all('a'):
                        dict['headlines']=n.text
                        dict['link']=n.get('href')
                        
                for m in k.find_all('aside',{'class':'flags top'}):
                    for l in m.find_all('dd'):
                        f=l.text
                        d=str(datetime.datetime.strptime(f,'\n\n           %d %b %Y       \n'))
                        dict['date']=d
                        
                for o in k.find_all('div'):
                    for p in o.find_all('p',{'class':'summary medium'}):
                        dict['descrip']= p.text
                arr.append(dict)
                collection.insert_one(dict)
#BBC END
                        

#BLOOMBERG START

e=entry.split(" ")
#print(e)
fin='+'.join(e)

#print("----------BLOOMBERG NEWS-----------")
dateCnt = 0
headCnt = 0
linksCnt = 0
descCnt = 0
for d in range(1,30):
    page=urllib2.urlopen('https://www.bloomberg.com/search?query='+fin+'&endTime=2018-05-21T06:34:12.628Z&page='+str(d)).read()
    soup=bs.BeautifulSoup(page,'lxml')
    #print("page"+str(d))
    li=[]
    count=0
    for i in soup.find_all('div',{'class':'container'}):
        for j in i.find_all('main',{'id':'content'},{'class':'main-content'}):
            for k in j.find_all('section',{'class':'content-stories'}):
                for l in k.find_all('div',{'class':'search-result-story__container'}):
                    dict={}   
                    for o in l.find_all('div',{'class':'search-result-story__metadata'}):
                        for p in o.find_all('span',{'class':'metadata-timestamp'}):
                            for q in p.find_all('time',{'class':'published-at'}):
                                if len(li)<=10:
                                    li.append(q.text)
                                     
                    for m in l.find_all('h1',{'class':'search-result-story__headline'}):
                        for n in m.find_all('a'):
                            #print("*******************")
                            dict['headlines']=n.text
                            dict['link']=n.get('href')
                            dt2=li[count]
                            dt3=datetime.datetime.strptime(dt2,' %b %d, %Y ')
                            dict['date']=str(dt3)
                            headCnt+=1
                            linksCnt+=1
                            dateCnt+=1
                            count=count+1
                            
               
                    for r in l.find_all('div',{'class':'search-result-story__body'}):
                        dict['descrip']=r.text
                        descCnt+=1
                            
                    arr.append(dict)
                    collection.insert_one(dict)
#bloomberg end   

                  
#NYTimes Start
                    
e=entry.split(" ")
#print(e)
fin='%20'.join(e)   


#print("----------NEWYORK TIMES----------")

dateCnt = 0
headCnt = 0
linksCnt = 0
descCnt = 0

for z in range(0,1):
    page=urllib2.urlopen('https://www.nytimes.com/search?query='+fin+'&sort=best').read()
    soup=bs.BeautifulSoup(page,'lxml')
    for i in soup.find_all('div',{'id':'app'}):
        for n in i.find_all('div',{'class':'Item-item--2UnE8'}):
            for o in n.find_all('div',{'Item-wrapper--2ba8L'}):
                dict={}
                for j in o.find_all('a'):
                    link=j.get('href')
                    flag=0
                    if link.startswith('https'):
                        flag=1
                    if (link.endswith('html') and flag==0):
                        #print("**************")
                        dict['link']=link
                        linksCnt+=1
                    no=link.find('2')
                    if(no>=0):
                       dt4=link[no:11]
                       if dt4=='20':
                           da=None
                           #print(" DATE : NIL")
                       else:
                           c=str(datetime.datetime.strptime(dt4,'%Y/%m/%d'))
                           da=c 
                        
                        
                    else:
                        da=None
                        
                    dict['date']=da
                    dateCnt+=1
                for k in o.find_all('h4',{'class':'Item-headline--3WqlT'}):
                    dict['headlines']=k.text
                    headCnt+=1
                 
                for l in o.find_all('p',{'class':'Item-summary--3nKWX'}):
                    dict['descrip']=l.text 
                    descCnt+=1
            arr.append(dict)
            collection.insert_one(dict)
                
          
                
#NYTimes end

#TIMESOFINDIA start
                        
                        
e=entry.split(" ")
#print(e)
fin='-'.join(e)   



#print("----------TIMES OF INDIA----------")

for z in range(0,1):
    page=urllib2.urlopen('https://timesofindia.indiatimes.com/topic/'+fin+'/news/'+str(z)).read()
    soup=bs.BeautifulSoup(page,'lxml')
    #print(soup.prettify())
    for i in soup.find_all('div',{'class':'content'}):
        dict={}
        for k in i.find_all('span',{'class':'title'}):
            #print(k.prettify)
            #print("*****************")
            dict['headlines']=k.text
            
            
            
        for j in i.find_all('a'):
            dict['link']=j.get('href')
            for l in j.find_all('span',{'class':'meta'}):
                dd=l.text
                            
                f=dd.find('Z')
                if f>=0:
                    da1=dd[:10]

                else:
                    c=str(datetime.datetime.strptime(dd,'%d %b %Y'))
                    da1=c
                dict['date']=da1                        
            for m in j.find_all('p'):
                dict['descrip']=m.text
        arr.append(dict)
        collection.insert_one(dict)    
#TIMESOFINDIA End
                
                
#CNBC START
                
e=entry.split(" ")
#print(e)
fin='%20'.join(e)  




#print("----------CNBC NEWS----------")


for z in range(0,1):
    page=urllib2.urlopen('https://search.cnbc.com/rs/search/view.html?target=all&categories=exclude&partnerId=2000&keywords='+fin).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for i in soup.find_all('div',{'class':'SearchResultCard'}):
        #print(i.prettify())
        dict={}
        for j in i.find_all('h3',{'class':'title'}):
            #print(j.prettify())
            for k in j.find_all('a'):
                #print("*****************")
                dict['headlines']=k.text
                linnk=k.get('href')
                dict['link']=linnk
                lin_k=linnk.split("com/")
                linnnk=lin_k[1]
                no=linnnk.find('2018')
                if no>=0:
                    #print("DATE : "+linnnk[:10])
                    d=linnnk[:10]
                    dt4=linnnk[:10]
                    d=str(datetime.datetime.strptime(dt4,'%Y/%m/%d'))
                    da2=d
                else:
                    da2=None
                dict['date']=da2
                
                
                        
        for l in i.find_all('p',{'class':'description'}):
            dict['descrip']=l.text
        arr.append(dict) 
        collection.insert_one(dict)
        

#CNBC END



#finalDict={"data":arr}  


