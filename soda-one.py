import cx_Oracle
import myConnectInfo
connection = cx_Oracle.connect(myConnectInfo.usrnm, myConnectInfo.psswd, myConnectInfo.dsn)

print("\nDatabase version:", connection.version)

# Enable Auto-commit
connection.autocommit = True

# Create the parent object for SODA
soda = connection.getSodaDatabase()
 
# Create a new SODA collection
# This will open an existing collection, if the name is already in use.
collection = soda.createCollection("sodacollection")
 
# Clean up the collection if it already exists and contains documents
collection.find().remove()

# Insert some documents into the collection
content = {'name': 'Koala', 'infraclass': 'marsupialia', 'family': 'Phascolarctidae'}

doc = collection.insertOneAndGet(content)

# Display the Key for the latest entry
key = doc.key
print('\nThe key of the new SODA document is: ', key)

# Return the most recent entry (using the key)
content = collection.find().key(key).getOne().getContent()
print(content)

# Close the database connection
connection.close()
