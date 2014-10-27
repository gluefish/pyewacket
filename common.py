import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import gspread
import urllib
import json
import datetime
import time

from time import *

def p(string):
    print string

#######################    gspread utils  ########################

def gsfind(obj, rowitem, colitem):
    rcval = obj.cell(obj.find(rowitem).row, obj.find(colitem).col).value
    return rcval
        
#######################  webdriver utils ########################
    
def findId(object,string):
    x = object.find_element_by_id(string)
    return x 

def setBrowser(string):
    if string == 'Firefox':
        x = webdriver.Firefox()
        return x
    if string == 'Chrome':
        x = webdriver.Chrome()
        return x  
    if string == 'PhantomJS':
        x = webdriver.PhantomJS('usr/bin/phantomjs')
           
def test_Exists():
    pass

def is_element_present(obj, how, what):
    try: obj.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def is_alert_present(self):
    try: 
        self.driver.switch_to_alert()
    except NoAlertPresentException, e: return False
    return True
        
def close_alert_and_get_its_text(self):
    try:
        alert_text = alert.Text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:  self.accept_next_alert = True
