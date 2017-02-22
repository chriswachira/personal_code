import sqlite3

class Database():
	def __init__(self, filename):
		"""initialize a database connection and create a database if none is found"""
		fn = filename + ".db"
		self._db = sqlite3.connect(fn)
		self.c = self._db.cursor()

	def create_table(self, table_name, fields, *args):
		"""creates a table for the specified table and fields for the table"""
		self.c.execute("DROP TABLE IF EXISTS {0}".format(table_name))
	#	for field, data_type in fields.items():
		#self.c.execute("CREATE TABLE ")

	def insert(self, table, values):
		"""inserts data into a specified table and with values in form of a tuple"""
		self.c.execute("INSERT INTO {0} VALUES {1}".format(table, values))
		self.commit()

	def sql_do(self, sql, *params):
		"""executes custom sql commands with or without sqlite3 parameters"""
		self.c.execute(sql, params)
		self.commit()	