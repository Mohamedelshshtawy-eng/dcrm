import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '6060',
    port = '3307',
    auth_plugin = 'mysql_native_password'
)

curser = mydb.cursor();

curser.execute("CREATE DATABASE elderco")


print('well done')