# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# 1: How many quakes are there in total?
def isQuake(data):
    if data["properties"]["type"] == "earthquake":
        return True
    return False


def cntQuakes(data):
    cnt = 0
    for quake in data:
        if isQuake(quake):
            cnt += 1
    return cnt


print(cntQuakes(data["features"]))

# following solution much easier / shorter as it does not need any function definition
print(
    sum(
        quake["properties"]["type"] is not None and quake["properties"]["type"] == "earthquake"
        for quake in data["features"]
    )
)

# following solution is even easier / shorter as it is part of the file itself
print(data["metadata"]["count"])

# 2: How many quakes were felt by at least 100 people?
print(
    sum(
        quake["properties"]["type"] is not None and quake["properties"]["type"] == "earthquake"
        and quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
        for quake in data["features"]
    )
)


# another solution
def feltreport(q):
    f = q["properties"]["felt"]
    return (f is not None and f >= 100)


feltreports = list(filter(feltreport, data["features"]))
print(len(feltreports))


# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getfelt(quakes):
    f = quakes["properties"]["felt"]
    if f is not None:
        return f
    return 0


mostfeltquake = max(data["features"], key=getfelt)
print(f"{mostfeltquake['properties']['title']}, {mostfeltquake['properties']['felt']}")


# 4: Print the top 10 most significant events, with the significance value of each
def getsig(quakes):
    s = quakes["properties"]["sig"]
    if s is not None:
        return s
    return 0


topsig = sorted(data["features"], key=getsig, reverse=True)
for i in range(0, 10):
    print(f"{topsig[i]['properties']['title']}, {topsig[i]['properties']['sig']}")
