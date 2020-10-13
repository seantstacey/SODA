import cx_Oracle
import myConnectInfo

connection = cx_Oracle.connect(myConnectInfo.usrnm, myConnectInfo.psswd, myConnectInfo.dsn)

# Enable Auto-commit
connection.autocommit = True


print("\nDatabase version:", connection.version)

cxcur = connection.cursor()

print("\n1. Create JSON Table called TEST_JSON and INSERT a row \n")
cxcur.execute('create table test_json (id number generated always as identity, json_data clob, check (json_data IS JSON))')

cxcur.execute('insert into test_json(json_data) values (\'{"firstName": "John", "lastName": "Smith" , "Age": 25, "address": {"street": "21 2nd street", "city": "New York", "state": "NY", "postalCode": "10021", "isBusiness": "false"}, "phoneNumbers": [{ "type": "home", "number": "212-555-1234"},{"type": "mobile", "number": "646-555-4567"}]}\')')

cxcur.execute('commit')

## Query table data once more time.
print("2. Display contents for JSON Table.\n")
cxcur.execute('select * from test_json')

for row in cxcur:
    print ( row)

print("\n3. Retrieve only the First Name.\n")
cxcur.execute('select json_value(json_data, \'$.firstName\') from test_json')

for row in cxcur:
    print ( row)

cxcur.close()
connection.close()
