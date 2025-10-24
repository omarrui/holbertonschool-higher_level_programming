#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all cities of that state"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cursor.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])
    print(", ".join(cities))
    cursor.close()
    db.close()
