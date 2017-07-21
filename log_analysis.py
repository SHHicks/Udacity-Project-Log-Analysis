#!/usr/bin/env python2
#
# Udacity Project: Log Analysis
# Author: Steve Hicks

import psycopg2

#######################
# SQL COMMAND STRINGS #
#######################

# SQL command to find the most popular three articles

POPULAR_ARTICLES_SQL = '''select a.title, count(*) as num
from articles a join log l
on ('/article/' || a.slug) = l.path
group by a.title
order by num desc
limit 3;'''

# SQL command to find the most popular article authors of all timestamp

POPULAR_AUTHORS_SQL = '''select au.name, count(*) as num
from articles ar join log l
on ('/article/' || ar.slug) = l.path
join authors au
on au.id = ar.author
group by au.name
order by num desc;'''

# SQL command to find the days with >1% ERRORS_SQL (calc'd in tenths of
# a percent)

ERRORS_SQL = '''
select * from (
  select to_char(day, 'Mon DD, YYYY') as fmt_day, bad * 10000 / total as error
  from (
    select  date(time) as day, count(*) as total,
    count(case when log.status = '404 NOT FOUND' then 1 else null end) as bad
    from log
    group by day
    ) as counts
  order by error desc
  ) as percent
where error > 100;'''

############################
# SQL EXECUTION & PRINTOUT #
############################

# connect to DB

db = psycopg2.connect('dbname=news')
c = db.cursor()

# execute the SQL command to find the three most popular articles

c.execute(POPULAR_ARTICLES_SQL)
results = c.fetchall()

# print results in proper format

print "\n1. What are the most popular three articles of all time?\n"
for row in results:
    print '"' + row[0] + '" - ' + str(row[1]) + ' views'

# execute the SQL command to find the most popular authors

c.execute(POPULAR_AUTHORS_SQL)
results = c.fetchall()

# print results in proper format

print "\n2. Who are the most popular article authors of all time?\n"
for row in results:
    print row[0] + ' - ' + str(row[1]) + ' views'

# execute the SQL command to find days had more than 1% requests in error

c.execute(ERRORS_SQL)
results = c.fetchall()

# print results in proper format

print "\n3. On which days did more than 1% of requests lead to errors?\n"
for row in results:
    print row[0] + ' - ' + '{:.1f}'.format(row[1]/100.0) + '% errors'

# close DB connection

print
db.close()
