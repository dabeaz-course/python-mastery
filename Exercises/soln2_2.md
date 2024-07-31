# Exercise 2.2 - Solution

There is no official solution for this exercise--you need rely on your
current Python knowledge.  However, there are a few tips that can
help.

- For problems where you need to determine uniqueness, use a set. Sets aren't allowed to
have duplicates.

- If you need to tabulate data, consider using a dictionary that maps keys to a numeric
count.  For example, to count rides on each bus route, you could make a dictionary that
maps the route name to the total ride count for that route.  A `Counter` object from
`collections` is perfect for this task.

- If you need to keep data in order or sort data, store it in a list.

- You can make Python data structures out of almost anything.  For
example, dictionaries of sets, nested dictionaries, etc.  You might
need to do this to answer questions 3 and 4.

Even though no code is provided, here are some answers to the questions
so that you can check your work:

1. How many bus routes exist in Chicago? (Answer: 181)

2. How many people rode the number 22 bus on February 2, 2011? (Answer: 5055)

3. What is the total number of rides taken on each bus route? (Answer: for the top three routes, [('79', 133796763), ('9', 117923787), ('49', 95915008)])

4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011? (Answer: [('15', 2732209), ('147', 2107910), ('66', 1612958), ('12', 1612067), ('14', 1351308)])

[Back](ex2_2.md)
