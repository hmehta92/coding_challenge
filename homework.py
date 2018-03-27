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