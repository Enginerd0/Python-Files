# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 19:25:22 2022

@author: Alexander Urbina
"""
import requests
from bs4 import BeautifulSoup
import openpyxl

def scrape_website(address: str) ->str:
    """
    Parameters
    ----------
    address : str
    Scrape the properties website and return the response text

    Returns str as response.txt
    -------
    str
        DESCRIPTION.
    """
    headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac "\ 
               "OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"}
        # try to keep  the headers on one line when writing the program 
        r = requests.get (address, headers=headers)
        return r.text
    soup = BeautifulSoup(response, features="lxml")