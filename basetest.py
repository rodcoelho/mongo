#!/usr/bin/env python3

import pymongo

try:
    conn = pymongo.MongoClient()
    # db = conn.userstable
    print('sucess')
except:
    print("fail")
conn.database_names()
