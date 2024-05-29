import pandas as pd
import mysql.connector
from sqlalchemy import create_engine


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
               return cursor,db_name
          except mysql.connector.Error as err:
            print("Database not found. Please enter a valid database name.")
     
        
#function to create a table
def create_table(cursor,column):
     command="CREATE TABLE "
     t_name=input("Enter the name of the table to be created:")
     command+=t_name+'('

     for i in range(len(column)):
          command+=column[i]+" "+input("Enter the datatype for "+column[i]+": ")
          if i<len(column)-1:
               command+=','
     command+=");"
     print(command)
     cursor.execute(command)
     print("Table create sucessfully")
     return cursor,t_name

#function to read excel data
def file_data(path):
     data=pd.read_excel(path)
     return data



def get_database_connection(database_name):
    engine = create_engine(f"mysql+mysqlconnector://test:test@127.0.0.1/{database_name}")
    return engine

# Get database connection
def enter_data(database_name,data,t_name):
      engine = get_database_connection(database_name)
      try:
        data.to_sql(name=t_name, con=engine, if_exists='append', index=False)
        print("Data inserted successfully.")
      except Exception as e:
        print(f"An error occurred: {e}")
          

