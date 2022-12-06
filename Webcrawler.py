 lines (188 sloc)  7.68 KB

import requests
from bs4 import BeautifulSoup
import re
from models import Coin
import urllib.request
import time
from functools import partial
import os
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from Files import create_dir, write_details

from bs4 import  NavigableString
from bs4 import  Tag

def scan_url_return_soup(url):
    source_code = multiprocessing.get(url)
    plain_text = multiprocessing.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    return soup
    
def scan_url_return_soup2(url):
    source_code = multiprocessing.get(url)
    plain_text = multiprocessing.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    return soup