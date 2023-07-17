# cta.py

from collections import defaultdict, Counter
import tracemalloc
import readrides

tracemalloc.start()

rows = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

# --------------------------------------------------
# Question 1:  How many bus routes are in Chicago?
# Solution: Use a set to get unique values. 

routes = set()
for row in rows:
    routes.add(row['route'])
print(len(routes), 'routes')

# --------------------------------------------------
# Question 2: How many people rode route 22 on February 2, 2011?
# Solution: Make dictionary with composite keys

by_route_date = { }
for row in rows:
    by_route_date[row['route'], row['date']] = row['rides']

print('Rides on Route 22, February 2, 2011:', by_route_date['22','02/02/2011'])

# --------------------------------------------------
# Question 3: Total number of rides per route
# Solution: Use a counter to tabulate things
rides_per_route = Counter()
for row in rows:
    rides_per_route[row['route']] += row['rides']

# Make a table showing the routes and a count ranked by popularity
for route, count in rides_per_route.most_common():
    print('%5s %10d' % (route, count))

# --------------------------------------------------
# Question 4: Routes with greatest increase in ridership 2001 - 2011
# Solution: Counters embedded inside a defaultdict

rides_by_year = defaultdict(Counter)
for row in rows:
    year = row['date'].split('/')[2]
    rides_by_year[year][row['route']] += row['rides']

diffs = rides_by_year['2011'] - rides_by_year['2001']
for route, diff in diffs.most_common(5):
    print(route, diff)

# ---- Memory use
print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
