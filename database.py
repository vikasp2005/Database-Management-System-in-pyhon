
import function as f


connection=f.connect_user()

cursor=connection.cursor()



file_path=f.select_file()
data=f.file_data(file_path)
print("The column names in excel sheel:")
column=list(data.columns)
for i in column:
    print(i)


cursor=f.connect_db(cursor)


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
f.enter_data(cursor,data,t_name)

connection.commit()