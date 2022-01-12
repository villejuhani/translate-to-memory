"""
@author: Ville Hytönen
@version: 12.1.2022
@state: In Development
"""

import sqlite3

# Query the database and return all records
def show_all():
	# Connects to database
	conn = sqlite3.connect('words.db')
	# Creates a cursor
	c = conn.cursor()
	
	# Query the database
	c.execute("SELECT * FROM words")
	items = c.fetchall()

	print("WORD " + "\tTRANSLATION " + "\tDEFINITION")
	print("-----" + "\t-----------" + "\t----------")
	for item in items:
		print(item[0] + "\t" + item[1] + "\t" + item[2])

	# Commits command
	conn.commit()

	# Closes connenction. Not necessary, but good practise.
	conn.close()


# Add a new record to the table
def add_one(search_word, translation, definition):
	conn = sqlite3.connect('words.db')
	c = conn.cursor()
	c.execute("INSERT INTO words VALUES (?, ?, ?)", (search_word, translation, definition))

	# Commits command
	conn.commit()

	# Closes connenction. Not necessary, but good practise.
	conn.close()


# Delete record from the table
def delete_one(id):
	conn = sqlite3.connect('words.db')
	c = conn.cursor()
	c.execute("DELETE from words WHERE rowid = (?)", id)

	# Commits command
	conn.commit()

	# Closes our connenction. Not necessary, but good practise.
	conn.close()	