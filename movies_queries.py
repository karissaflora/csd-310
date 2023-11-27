import mysql.connector
cnx = mysql.connector.connect(user='movies_user', password='Big69Qua',
                              host='localhost',
                              database='movies')
cursor = cnx.cursor()
query = "SELECT * from studio"
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Studio RECORDS--")
for row in result:
    print("Studio ID:",row[0])
    print("Studio Name:",row[1])
    print(" ")
query = "SELECT * from genre"
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
for row in result:
    print("Genre ID:",row[0])
    print("Genre Name:",row[1])
    print(" ")
query = "SELECT film_name,film_runtime from film where film_runtime<120 "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--")
for row in result:
    print("Film Name:",row[0])
    print("Runtime:",row[1])
    print(" ")
query = "SELECT film_name,film_director from film order by film_director "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Director RECORDS in Order--")
for row in result:
    print("Film Name:",row[0])
    print("Director:",row[1])
    print(" ")
cursor.close()
cnx.close()
