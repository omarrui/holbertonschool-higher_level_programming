#!/usr/bin/python3
import MySQLdb
import sys
"""
1-filter_states
lists all states from the
database hbtn_0e_0_usa
where name starts with 'n'
and is ordered by id (ascending)
"""


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch and print results
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
