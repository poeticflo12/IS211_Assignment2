# Assignment 2 IS211
import urllib.request
import urllib
import csv
import datetime
import logging
import argparse


# This reads and downloads the data from url that was given
def downloadData(url):
    url = urllib.request.urlopen(url)
    return url


logging.basicConfig(filename="errors.log", level=logging.ERROR)
logger = logging.getlogger("assignment2")


# Processes datafile in CSV format
def processData(file_data):
    showfile = csv.dictreader(file_data)
    newdict = {}
