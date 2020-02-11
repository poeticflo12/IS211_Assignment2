# Assignment 2 IS211
import urllib.request
import urllib
import csv
import datetime
import logging
import argparse


# This reads and downloads the data from url that was given
def downloadData(url):
    data = urllib.request.urlopen(url)
    return data


logging.basicConfig(filename="errors.log", level=logging.ERROR)
logger = logging.getLogger("assignment2_IS211")


# Processes datafile in CSV format
def processData(data):
    show = csv.DictReader(data)
    dictionary_new = {}

    for number, lines in enumerate(show):
        layout = "%d/%m%y"
        born = datetime.datetime.strptime(lines["birthday"], layout)
        dictionary_new[lines["identification"]] = (lines["name"], born)

        logging.error(
            "\nIssues Processing Line {} for ID# {}\n".format(number, lines["identification"]))

        return dictionary_new
