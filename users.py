from database import Database

class UsersDB():
	def __init__(self):
		"""connect to users.db database"""
		self._db = Database("users")
		self.c = self._db.cursor()

	def create_table(self):
		self.c.sql_do("""CREATE TABLE USERS 
			ID	INT 	PRIMARY KEY NOT NULL,
			USERNAME	CHAR(20)	NOT NULL,
			PASSWORD	CHAR(20)	NOT NULL,
			DATEOFCREATION	INT 	NOT NULL
			""")

	def insert_user(self):
		values = (1, "chriswachira", "1234567890", 1112016)
		self.c.insert("USERS", values)

	def fetch_user(self, key):
		row = self.c.sql_do("SELECT * FROM USERS WHERE USERNAME = {0}".format(key))
		print(row)

	def fetch_password(self, username):
		password = self.c.sql_do("SELECT PASSWORD FROM USERS WHERE USERNAME = {0}".format(username))
		return password

