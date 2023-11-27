import mysql.connector
#open a connection to the MySQL server and store the connection object in the variable cnx
cnx = mysql.connector.connect(user='movies_user', password='Big69Qua',
                              host='localhost',
                              database='movies')
try:
    db= mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],  config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if  err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
