#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        # Connect to the database
        db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        cursor = db.cursor()

        # Execute the query to fetch all states, sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        for state in cursor.fetchall():
            print(state)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
