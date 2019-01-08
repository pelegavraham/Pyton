import sys
import sqlite3
import os


def print_table(list_of_tuples):
    for item in list_of_tuples:
        print(item)


def main(args):

    databaseexisted = os.path.isfile('schedule.db')

    dbcon = sqlite3.connect('classes.db')

    with dbcon:
        cursor = dbcon.cursor()