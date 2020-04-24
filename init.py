import mysql.connector as mysql
import os
import subprocess

"""
Get's the current working directory, then gets the sqldump.sh file.
Syntax is - 
mysqldump db_name table_name > table_name.sql 
To use this, change any of the databse configuration settings. 
Also uses the mysql-connector package for python3.8. pip install mysql-connector-python 
If you wanted to use on any OS other than Linux, change the DB connector and your OS's equievelent for the sqldump.sh script 
"""

dir = os.getcwd()
dumpcmd = dir + "/sqldump.sh"

db = mysql.connect(
    host = "localhost",
    user = "USERNAME",
    passwd = "PASSWORD",
    database = "DATABASE_NAME"
)

passwd = "DATABASE PASSWORD"


cursor = db.cursor(buffered=True)

#	Calls the sheell command to sql dump, returns the output
def _sqldump(table_name):
    sp = subprocess.Popen([dumpcmd, db.user, passwd, db.database, table_name], stdout=subprocess.PIPE)
    out = sp.stdout.readline()
    return out

#	Shows all tables in given database, stores results in res
cursor.execute("SHOW TABLES")
res = cursor.fetchall()


with open("tables.txt", "w") as f:
	f.writelines("%s\n" % result for result in res)

with open("tables.txt") as f:
	for i in f:
		_sqldump(i)
