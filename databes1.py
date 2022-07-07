import psycopg2
mydb=psycopg2.connect(
    database="mahesh dahal",
    user="postgres",
    password="maipokhari1",
    host="localhost",
    port=5432,
)
cursor=mydb.cursor()
query="select * from student"
cursor.execute(query)
array=list(cursor.fetchall())
print(array)
print("given data is:")
for x in array:
    print(x)