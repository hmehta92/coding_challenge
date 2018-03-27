# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:59:36 2018

@author: Harshit Mehta
"""

# importing required packages
import os
from bs4 import BeautifulSoup
import re
import json
import time
start=time.time() # to see the time it takes for the entire work
# Changing directory to access files
directory="C:/Users/Harshit Mehta/Desktop/arthena/coding-challenge/lot-parser/data" # directory which contains both the folder
os.chdir(directory)

# Accessing files for both the year
filename=[file for file in os.listdir(".")]

# Accessing HTML files of each folder
file_2015=[file for file in os.listdir(filename[0])]
file_2017=[file for file in os.listdir(filename[1])]

# Creating function

#a) To start writing file
def reading(x):
    with open('stdout.json', 'w') as outfile:
        json.dump(x, outfile)
    return

#b) To append to existing json file
def append(x):
    with open('stdout.json', 'a') as outfile:
        outfile.write("\n")
        json.dump(x, outfile)
        outfile.write("\n")
    return

#c) to Scrap the data
def scrap(x,a):
    if x=="2015":
        html = open(filename[0]+"/"+a,'r').read()
    else:
        html = open(filename[1]+"/"+a,'r').read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup
# Part 1: To read the artist name

#1) created a list for year 2015
scrape_list_2015=[]
#2) Starting a loop to scrap all the five files
for i in file_2015:
    soup=scrap("2015",i)
    scrape_list_2015.append(soup.h2.string.split("(")[0].strip())
#3) Writing information to a file    
reading(scrape_list_2015)

# part 2: To read artist name and work
scrape_list_2015=[]
for i in file_2015:
    soup=scrap("2015",i)
    scrape_list_2015.append({"artist":soup.h2.string.split("(")[0].strip(),"works":[{"title":soup.h3.string}]})
# Appending to the file started in part 1 
append(scrape_list_2015)

# part 3: To read artist name, work and priee
scrape_list_2015=[]
for i in file_2015:
    soup=scrap("2015",i)
    scrape_list_2015.append({"artist":soup.h2.string.split("(")[0].strip(),"works":[{"title":soup.h3.string,"price":soup.find_all("div")[1].string}]})
# Appending to the file started in part 1 
append(scrape_list_2015)

# Part 4:  to read artist name, work, currency and amount
scrape_list_2015=[]
for i in file_2015:
    soup=scrap("2015",i)
    scrape_list_2015.append({"artist":soup.h2.string.split("(")[0].strip(),"works":[{"title":soup.h3.string,"currency":soup.find_all("div")[1].string.split(" ")[0],
                                        "amount":int(re.sub(",","",soup.find_all("div")[1].string.split(" ")[1]))}]})
# Appending to the file started in part 1 
append(scrape_list_2015)

# Part 5: To get details from year 2017 folder
scrape_list_2017=[]
for i in file_2017:
    soup=scrap("2017",i)        
    scrape_list_2017.append({"artist":soup.find_all("h3")[0].string.split("(")[0].strip(),"works":[{"title":soup.find_all("h3")[1].string,
                                        "currency":soup.find_all("div")[1].span.string,
                                        "amount":int(re.sub(",","",soup.find_all("div")[1].find_all("span")[1].string))}]})
# Appending to the file started in part 1 
append(scrape_list_2017)

# Part 6: Combining data from both files
list1=scrape_list_2015+scrape_list_2017
artist = []
list2 = []
for z,i in enumerate(list1):
    x = [item for item in artist if i['artist'] in item]
    if x:
        if i['works'][0]['currency']=='GBP':
            i['works'][0]['currency']='USD'
            i['works'][0]['amount']*=1.34
            
        [item[1] for item in list2 if x[0][0] in item][0]['works'].append(i['works'][0])
    else:
        if i['works'][0]['currency']=='GBP':
            i['works'][0]['currency']='USD'
            i['works'][0]['amount']*=1.34
        artist.append((z,i['artist'])) #adding artist to checklist
        list2.append((z,i))              # updating penultimate json list
list3 = []
for s,t in list2:
    list3.append(t)
final_combined =list3
for z,i in enumerate(final_combined):
    total = 0
    for item in i['works']:
        total += item['amount']
    final_combined[z]['total amount'] = final_combined[z]['works'][0]['currency'] +' ' +"{:,}".format(total)
# Appending to the file started in part 1 
append(final_combined)
print("Completed in time {}".format(time.time()-start))
