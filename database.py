import mysql.connector
import function as f


connector=f.connect_user()

cursor=connector.cursor()


#cursor=f.connect_db(cursor)


data=f.file_data('C:/Users/pviki/programing/pythonProject/databaseproject/dbms.xlsx')
print("The column names in excel sheel:")
column=list(data.columns)
for i in column:
    print(i)
