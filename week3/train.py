"""
Created on Thu Oct  8 19:52:23 2020

@author: sinead
"""

import requests
import csv
from bs4 import BeautifulSoup
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
with open('week03_train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("objTrainPositions")
    for listing in listings:
        lat =float( listing.TrainLatitude.string)
        if (lat < 53.4):
            entryList = []
            for retrieveTag in retrieveTags:
                entryList.append(listing.find(retrieveTag).string)
            train_writer.writerow(entryList)   
    

