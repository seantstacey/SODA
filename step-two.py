import cx_Oracle
import myConnectInfo

connection = cx_Oracle.connect(myConnectInfo.usrnm, myConnectInfo.psswd, myConnectInfo.dsn)

print("Database version:", connection.version)

results = connection.cursor()
results.execute('select * from dept') 

print('\nDEPT table contents:')
for row in results:
    print (row)

results.close()
connection.close()
