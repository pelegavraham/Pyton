import os
import sqlite3
import sys


def print_table(list_of_tuples):
    for item in list_of_tuples:
        print(item)


def main(args):

    databaseexisted = os.path.isfile('schedule.db')

    dbcon = sqlite3.connect('schedule.db')

    with dbcon:
        cursor = dbcon.cursor()
        if not databaseexisted:  # First time creating the database. Create the tables
            cursor.execute(
                "CREATE TABLE courses(id INTEGER PRIMARY KEY,"
                " course_name TEXT NOT NULL, student TEXT NOT NULL, number_of_students INTEGER NOT NULL, "
                "class_id INTEGER REFERENCES classrooms(id), course_length INTEGER NOT NULL)")  # create table courses
            cursor.execute(
                "CREATE TABLE students(grade TEXT PRIMARY KEY, count INTEGER NOT NULL)")  # create table students
            cursor.execute(
                "CREATE TABLE classrooms(id INTEGER PRIMARY KEY,"
                " location TEXT NOT NULL, current_course_id INTEGER NOT NULL, "
                "current_course_time_left INTEGER NOT NULL)")  # create table classrooms
            inputfilename = args[0]
            with open(inputfilename) as inputfile:
                for line in inputfile:
                    result = [x.strip() for x in line.split(',')]   #split line by comma.
                    tableName = result[0]
                    if tableName is "C":
                        cursor.execute("INSERT INTO courses VALUES (?,?,?,?,?,?)",
                                       (result[1], result[2], result[3], result[4], result[5], result[6]))
                    elif tableName is "S":
                        cursor.execute("INSERT INTO students VALUES (?,?)", (result[1], result[2]))
                    else:
                        cursor.execute("INSERT INTO classrooms VALUES (?,?)", (result[1], result[2]))

            print("courses table: ")
            cursor.execute("SELECT * FROM courses")
            courseslist = cursor.fetchall()
            print (print_table(courseslist))

            print("students table: ")
            cursor.execute("SELECT * FROM students")
            studentslist = cursor.fetchall()
            print (print_table(studentslist))

            print("classrooms table: ")
            cursor.execute("SELECT * FROM classrooms")
            classroomslist = cursor.fetchall()
            print (print_table(classroomslist))


if __name__ == '__main__':
    main(sys.argv)