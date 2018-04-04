#!/usr/bin/env python3

from pymongo import MongoClient
from pprint import pprint


def insert_one():
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


def insert_many():
    pass


def update_one():
    one_or_many = input('\n Select 1 for one update, or 2 for many updates\n')
    column = db.column_name
    key = input('\nkey term: ')
    value = input('\nvalue term: \n')
    try:
        if int(one_or_many) == 1:
            column.update_one({key: value})
        else:
            column.update_many({key: value})
    except:
        print('Update error')


def update_many():
    pass


def read_one():
    try:
        column = db.column_name
        key = input('\nkey term: ')
        value = input('\nvalue term: \n')
        pprint(column.find_one({key: value}))
    except:
        print('Read error')


def read_many():
    try:
        column = db.column_name
        print(list(column.find()))
    except:
        print('Read many error')


def delete_one():
    pass


def delete_many():
    pass


def main():
    while True:
        selection = input('\nSelect:\n1 to insert_one, 11 to insert_many,\n2 to update_one, 22 to update_many,\n3 to read_one, 33 to read_many,\n4 to delete_one, 44 to delete_many\n')

        if selection == '1':
            insert_one()
        elif selection == '11':
            insert_many()
        elif selection == '2':
            update_one()
        elif selection == '22':
            update_many()
        elif selection == '3':
            read_one()
        elif selection == '33':
            read_many()
        elif selection == '4':
            delete_one()
        elif selection == '44':
            delete_many()
        else:
            print('\nEXIT\n')
            break


if __name__ == '__main__':
    # connection to Mongo
    conn = MongoClient('localhost', 27017)
    # connection to database
    db = conn.useful_database_name
    main()
    conn.close()

