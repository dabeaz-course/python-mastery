from collections import Counter, defaultdict

import readrides

rows = readrides.read_rides_as_dicts("Data/ctabus.csv")

# How many bus routes exist in Chicago?
routes = {row["route"] for row in rows}
print("How many bus routes exist in Chicago?", len(routes))

# How many people rode the number 22 bus on February 2, 2011?
# What about any route on any date of your choosing?
rides_by_route_date = {}
for row in rows:
    rides_by_route_date[row["route"], row["date"]] = row["rides"]
print(f"Passengers for route 22 on 01/02/2011:", rides_by_route_date["22", "01/02/2011"])

# What is the total number of rides taken on each bus route?

rides_per_route = Counter()
for row in rows:
    rides_per_route[row["route"]] += row["rides"]
for route, rides in rides_per_route.most_common(10):
    print(f"{route:5s} {rides:10d}")

# What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
rides_by_year = defaultdict(Counter)
for row in rows:
    year = row["date"].split("/")[2]
    rides_by_year[year][row["route"]] += row["rides"]
diffs = rides_by_year["2011"] - rides_by_year["2001"]
for route, diff in diffs.most_common(5):
    print(route, diff)
