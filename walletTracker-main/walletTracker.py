#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:10:20 2021

@ygoats
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import telegram_send
from time import sleep
from datetime import datetime

oneList = []

now = datetime.now()
t = now.strftime("%m/%d/%Y, %H:%M:%S")

print("Connection Established Wallet Tracker")
print(str(t))

####### vvvvvvvvvv the wallet vvvvvvvvvvvvvvvvvvv
####### 0xa15cc90d0b37cc17b27aa5d35702ee85ff646ddb
####### can be replaced with any wallet to track

url = 'https://bscscan.com/address/0xa15cc90d0b37cc17b27aa5d35702ee85ff646ddb'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

page_soup = soup(webpage, "html.parser")

containers = page_soup.findAll("td", "d-none d-sm-table-cell")

blockOne = containers[0]
blockOne = str(blockOne)
oneList.append(blockOne)

twoBlocksConfirmed = True


while twoBlocksConfirmed == True:
    sleep(3)
    url = 'https://bscscan.com/address/0xa15cc90d0b37cc17b27aa5d35702ee85ff646ddb'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    
    page_soup = soup(webpage, "html.parser")
    
    containers = page_soup.findAll("td", "d-none d-sm-table-cell")
    
    blockNew = containers[0]
    blockNew = str(blockNew)
    
    if blockNew not in oneList:
        oneList.append(blockNew)
        print('New Transaction Found!')
        
        url = 'https://bscscan.com/address/0x57ef04f9dfc334956cb346a33512bbe383850a54722e71c4d603b5ad317bc3b8'
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        page_soup = soup(webpage, "html.parser")
        containers = page_soup.findAll("a", "hash-tag text-truncate myFnExpandBox_searchVal")
        txnAdd = str(containers[0]['href'])
        txnAdd = txnAdd.replace('/tx/', '')

        telegram_send.send(disable_web_page_preview=True, conf='user1.conf',messages=["Degen 1 Has Made a Transaction" + "\n" + \
                                                       "https://bscscan.com/tx/" + str(txnAdd)])
