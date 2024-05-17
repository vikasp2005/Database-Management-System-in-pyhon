import pandas as pd
import mysql.connector


#function to connect to user in database
def connect_user():
     connector=mysql.connector.connect(
         host="127.0.0.1",
         user="test",
         password="test"
     )
     return connector

def connect_db(cursor):
     while True:
          try:
               db_name=input("Enter a database to connect:")

               cursor.execute("USE {}".format(db_name))
            
               # If execution reaches here, the database exists
               print("Connected to database:", db_name)
               return cursor
          except mysql.connector.Error as err:
            print("Database not found. Please enter a valid database name.")
        


#function to read excel data
def file_data(path):
     data=pd.read_excel(path)
     return data
