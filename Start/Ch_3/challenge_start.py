# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime
import pprint


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def getsig(dataitem):
    significance = dataitem["properties"]["sig"]
    if (significance is None):
        significance = 0
    return int(significance)


sorteddata = sorted(data["features"], key=getsig, reverse=True)
sorteddata = sorteddata[:40]
sorteddata.sort(key=lambda e: e["properties"]["time"], reverse=True)

header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map Link"]
rows = []

for event in sorteddata:
    thedate = datetime.date.fromtimestamp(int(event["properties"]["time"]) / 1000)
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][2]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"
    rows.append([
        event["properties"]["mag"],
        event["properties"]["place"],
        0 if event["properties"]["felt"] is None else event["properties"]["felt"],
        thedate,
        gmaplink
    ])

with open("significantevents.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)