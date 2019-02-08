# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:00:56 2019

@author: amar.lad
"""
import csv
import os
import json
import logging

from geopy.geocoders import Nominatim

#   sys.stdout = open('JASON_store_latitude_longitude.txt','wt')

data = {}
data['location'] = []   
keywords = ["SUITE", "SPACE", "STORE", "UNIT", "BLDG"]
READ_MODE = 'r'
geolocator = Nominatim(user_agent="store_latitude_longitude")
BASEDIR = "C:/Users/amar.lad/Desktop/Sephora" 
csvFilename = 'locationAddressUS.csv'

def readCSV(csvBASEDIR, csvFilename):
    reader = None
    try:
#        with open(os.path.join(csvBASEDIR, csvFilename), READ_MODE) as csvfile:
#            reader = csv.reader(csvfile)
        csvfile = open(os.path.join(csvBASEDIR, csvFilename))
        reader = csv.reader(csvfile)
    except IOError:
        logging.exception('')
    if not reader:
        raise ValueError('No data available')
    return reader

def checkWords(parm_row, parm_digit = None):
    returnString = ' '
    if not (any(keyword in parm_row for keyword in keywords) and parm_row):
        if parm_digit is not None:
            if any(c.isdigit() for c in parm_row):
                returnString = parm_row + ','
        else:
            returnString = parm_row + ','
    return returnString
        
csvReader = readCSV(BASEDIR, csvFilename)
next(csvReader, None)

for row in csvReader:
    string = ' '
    if row[1]:
        string = checkWords(row[1], True).strip()
    if row[2]:
        string += checkWords(row[2]).strip()
    if row[3]:
        string += checkWords(row[3]).strip()
    if row[4]:
        string += row[4] + ','  
    if row[5]:
        string += row[5] + ','
    if row[6]:       
        string += row[6][:5] + ','    
    if row[7]:       
        string += row[7]         
    
    location = geolocator.geocode(string, timeout=50)
    if location:
#        a = '}, {'
#        b = '   ' + 'position: new google.maps.LatLng(' + repr(location.latitude) + ',' + repr(location.longitude) + '),'
#        c = "    type: 'info'"
#        print(a)
#        print(b)
#        print(c)
        data['location'].append({
            'store': int(row[0]),
            'latitude': location.latitude,
            'longitude': location.longitude,
            'address': string})

with open('JASON_store_latitude_longitude.txt', 'w') as outfile:  
    json.dump(data, outfile, indent=4)