#example of python connecting to MySQL server and databases
#
import mysql.connector
#
from mysql.connector import Error
#
try:
    connection = mysql.connector.connect(host='129.10.79.239',
                                         database='world',
                                         user='studentuser',
                                         password='DBMS*spring2022',
                                         auth_plugin = 'mysql_native_password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
#
        sql_select_Query = "select CountryCode from countrylanguage where language = 'english'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Countries with english language:\n")
        for row in records:
            print('CountryCode =',row[0],"\n")
#
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#you should see the following output
#'''Connected to MySQL Server version  8.0.17
#Your connected to database:  ('classicmodels',)
#True
#MySQL connection is closed'''
#
