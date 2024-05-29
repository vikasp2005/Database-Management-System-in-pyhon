
import function as f


connector=f.connect_user()

cursor=connector.cursor()




data=f.file_data("C:/Users/pviki/programing/pythonProject/Database-Management-System-in-python/dbms.xlsx")
print("The column names in excel sheel:")
column=list(data.columns)
for i in column:
    print(i)


cursor,db_name=f.connect_db(cursor)
t_name=""
while True:
  present=input("Table already present or not ,Enter yes or No:")
  if present.lower()=='yes':
    t_name=input("Enter the name of the table:")
    break
  elif present.lower()=='no':
    cursor,t_name=f.create_table(cursor,column)
    break
  else:
     print("Enter the valid option")
f.enter_data(db_name,data,t_name)