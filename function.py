import pandas as pd
import mysql.connector
from tkinter import filedialog


#function to connect to user in database
def connect_user():
     connection=mysql.connector.connect(
         host="127.0.0.1",
         user="test",
         password="test"
     )
     return connection

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

     cursor.execute(command)
     print("Table create sucessfully")
     return cursor,t_name

#function to read excel data
def file_data(path):
     data=pd.read_excel(path)
     return data



def select_file():
    while True:
         # Open a file dialog and allow the user to select a file
         file_path = filedialog.askopenfilename()
    
         # Check if a file was selected
         if file_path:
           # Print the file path to the console
           return file_path

         else:
             # Print a message if no file was selected
             print("No file selected.")






# Get database connection
def enter_data(cursor,data,t_name):
      for _,row in data.iterrows():
          query=f"Insert into {t_name} values("
          for i in data:
               query+=f"\'{row[i]}\',"
          query=query.rstrip(',')
          query+=");"
     
          cursor.execute(query)
          

