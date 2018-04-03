#!/usr/bin/env python3

from pymongo import MongoClient
from pprint import pprint


def insert():
    try:
        column = db.column_name
        # prep/get data for payload
        userId = input('Enter Employee id :')
        userName = input('Enter Name :')
        userAge = input('Enter age :')
        userCountry = input('Enter Country :')

        # payload insert to users table
        payload = {
                "id": userId,
                "name": userName,
                "age": userAge,
                "country": userCountry
            }
        column.insert(payload)
        print('\nInserted data successfully\n')
        pprint(payload)

    except:
        print('Insert error')


def update():
    pass


def read():
    try:
        column = db.column_name
        key = input('\nkey term: ')
        value = input('\nvalue term: \n')
        pprint(column.find_one({key: value}))
    except:
        print('Read error')





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
            print('\n EXIT \n')
            break


if __name__ == '__main__':
    # connection to Mongo
    conn = MongoClient('localhost', 27017)
    # connection to database
    db = conn.useful_database_name
    main()
    conn.close()

