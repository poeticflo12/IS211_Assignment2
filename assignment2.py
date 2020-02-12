# Assignment 2 IS211
# url =  "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
import urllib.request
import urllib
import csv
import datetime
import logging
import argparse


# This reads and downloads the data from url that was given
def downloadData(url):
    # downloads contents
    info = urllib.request.urlopen(url).read().decode
    return info


dictionary_new = {}


# logging.basicConfig(filename="errors.log", level=logging.ERROR)
# 1logger = logging.getLogger("assignment2_IS211")


# Processes datafile in CSV format
# Takes the content and processes it line by line
def processData(files):
    csv_show = csv.DictReader(files)
    next(csv_show)

    for number, lines in enumerate(csv_show):
        # convert string to date
        layout = "%d/%m%y"
        born = datetime.datetime.strptime(lines[2], layout)
        dictionary_new[lines[1]] = (lines["name"], born)

        logging.error(
            "\nIssues Processing Line {} for ID# {}\n".format(number, lines["identification"]))


def displayPerson(id, personData=dictionary_new):
    if id in personData.keys():
        print(" Persons {} is {} with a birthday of {}".format(id, personData[id][0], personData[id][1]))
    else:
        print(" user not found with that id")
        # "No user found with that id”

        try:
            response = "Person ID #{idnumber} is {name} with a birthday of {date}"
            print(response.format(idnum=id, name=personData[id][0], date=personData[id[1]]))
        except KeyError:
            print(" user not found ")


def main():
    logger = logging.getLogger("assignment2_IS21ll")
    fh = logging.FileHandler('errors.log')
    fh.setLevel(logging.ERROR)
    logger.addHandler(fh)
    # Initialize parser
    commandParser = argparse.ArgumentParser(description="Send the ­­url parameter to the script")
    # add parameter
    commandParser.add_argument("--url", type=str, help="Linking csv file")
    # parse the argument
    args = commandParser.parse_args()
    # if url is not given
    if not args.url:
        exit()

        # call downloadData function and store in csvData
        try:
            csvData = downloadData(args.url)
        except:
            # if an error occurs print message and exit application
            print("An error has occured. Please try again")
            exit()
        # take csvData and pass it to processData and save it to personData
        personData = processData(csvData)


isTrue = True
while isTrue:
    n = input("Enter ID: ")
    if int(n) > 0:
        displayPerson(n)
    else:
        isTrue = False

if __name__ == "__main__":
    main()
