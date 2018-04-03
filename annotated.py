#!/usr/bin/env python3

from pymongo import MongoClient

######################################## create connection ###############################################
# if working with a remote server, provide the IP Address as opposed to 'localhost'
conn = MongoClient('localhost', 27017)


######################################## create a database ###############################################
# option 1
db = conn.testdb

# option 2
# db = client['testdb']


######################################## access a column in the database #################################
# option 1
column = db.column_name

# option 2
# column = db['column_name']


######################################## query data in a column ##########################################
data = testdb.column_name.find()
for d in data:
    print('unpack the dictionary here')


######################################## add 'documents' to a table ########################################
payload = {'info1': 'data1', 'info2': 'data2', 'info3': 'data3'}
column.insert(payload)


######################################## update data ######################################################
# update one or many
db.column_name.update_one(
    {"info1": "data1"}      # ... etc
)
db.column_name.update_many(
    {"info1": "data1"}      # ... etc
)

# delete one or many
db.column_name.delete_one(
    {"info1": "data1"}      # ... etc
)
db.column_name.delete_many(
    {"info1": "data1"}      # ... etc
)

######################################## close connection #################################################
conn.close()

