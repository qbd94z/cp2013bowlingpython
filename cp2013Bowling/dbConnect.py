print("Hello World")
import pymongo

print("Pymongo Imported")

dbURI = "mongodb://ben:test1234@kahana.mongohq.com:10098/cp2013Bowling"
connection = pymongo.Connection(dbURI)
print("Connection Successful")

db = connection.get_default_database()
print(db)

connection.