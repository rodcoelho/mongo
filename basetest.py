#!/usr/bin/env python3

from pymongo import MongoClient

#### create connectionm ####
# if working with a remote server, provide the IP Address as opposed to 'localhost'
conn = MongoClient('localhost', 27017)


#### create a database ####
# option 1
db = conn.testdb

# option 2
# db = client['testdb']


#### access a column in the database ####
# option 1
column = db.column_name

# option 2
# column = db['column_name']


#### query data in a column ####
testdb.column_name.find()


#### add 'documents' to a table ####
payload = {'info1': 'data1', 'info2': 'data2', 'info3': 'data3'}
column.insert(payload)


#### close connection ####
conn.close()


