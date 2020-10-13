import cx_Oracle
connection = cx_Oracle.connect('scott/<mypassword>@pdb1')

print("Database version:", connection.version)

results = connection.cursor()
results.execute('select * from dept') 

print('\nDEPT table contents:')
for row in results:
    print (row)

results.close()
connection.close()
