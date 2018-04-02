#!/usr/bin/env python3

from pymongo import MongoClient
from pprint import pprint

# connection to Mongo
client = MongoClient('/data/db')
# connection to database
db = client.useful_database_name

def insert():
    try:
        # prep/get data for payload
        userId = input('Enter Employee id :')
        userName = input('Enter Name :')
        userAge = input('Enter age :')
        userCountry = input('Enter Country :')

        # payload insert to users table
        payload = db.users.insert_one(
            {
                "id": userId,
                "name": userName,
                "age": userAge,
                "country": userCountry
            })

        print('\nInserted data successfully\n')
        pprint(payload)

    except:
        print('Insert error')


def update():
    pass


def read():
    pass


def delete():
    pass


def main():
    while True:
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print('\n INVALID SELECTION \n')


if __name__ == '__main__':
    main()

