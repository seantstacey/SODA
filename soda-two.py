import cx_Oracle
import myConnectInfo
connection = cx_Oracle.connect(myConnectInfo.usrnm, myConnectInfo.psswd, myConnectInfo.dsn)

# Enable Auto-commit
connection.autocommit = True

# Create the parent object for SODA
soda = connection.getSodaDatabase()
 
# Create a new SODA collection
# This will open an existing collection, if the name is already in use.
collection = soda.createCollection("sodacollection")
 
# Insert multiple documents into the collection
inDocs = [
    dict(name='Red Kangaroo', infraclass= 'marsupialia', family= 'Macropod'),
    dict(name='Emu', infraclass= 'aves', family= 'Casuariidae'),
    dict(name='Dingo', infraclass= 'mammalia', family= 'Canidae'),
    dict(name='Platypus', infraclass= 'marsupialia', family= 'Ornithorhynchidaea'),
    dict(name='Inland Taipan', infraclass= 'reptilia', family= 'Elapidae', venomous= 'Yes')
]

# Perform BULK insert
bulkDocs = collection.insertManyAndGet(inDocs)
for doc in bulkDocs:
   print("Inserted SODA document with key", doc.key)
print()

# Return the most recent entry (using the key)
content = collection.find().key(doc.key).getOne().getContent()
print("Last Inserted SODA document", content)

# Find all documents with infraclass containing 'marsupial%'
print("\ninfraclass names matching 'marsupial%'")
qbe = {'infraclass': {'$like': 'marsupial%'}}
for doc in collection.find().filter(qbe).getDocuments():
    content = doc.getContent()
    print(content["name"] + ",", "key:", doc.key)

# Close the database connection
connection.close()

