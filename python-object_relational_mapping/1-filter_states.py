#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()

    # Execute the query to fetch states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE TRIM(name) LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    # Print each state
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
