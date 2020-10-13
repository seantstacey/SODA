# SODA
Sample Python scripts to demonstrate SODA

This repo provides sample code to supplement a 3 part series from the blog site: https://seanstacey.org/?page_id=261

Part One of the Series covers the basics of connecting a Python program to an Oracle database using cx_Oracle.  The following scripts are used in Part One.

**MyConnectInfo.py**
 - This script holds the login credentials to connect to the Oracle Database.
   
**step-one.py**
 - This script demonstrates connecting from Python to Oracle using the cx_Oracle module and then querying a relational table to print the rows in Python.
 
**step-two.py**
 - This script builds upon the step-one.py script. It uses the MyConnectInfo.py to connect to the Oracle database.
 
**step-three.py**
 - This script demonstrates creating an Oracle table that contains a JSON Document.  It then performs a SQL insert into the table including a JSON entry. The data is then queried using two different approaches.
 
 
Part Two of the Series covers the use of Python and SODA
 
**soda-one.py**
 - This script uses SODA to create collection, inserts a document into the collection and displays the contents of the collection.
  
**soda-two.py**
 - This script performs a bulk insert into SODA collection and displays the ID for newly inserted document.  It then has a Query By Example where it filters the collection for a specific element.
  
**soda_query.sql**
 - A SQL script used to display the contents of the SODA collection created in the two SODA-python scripts. It is used before and after creating the collection to verify the creation of the collection from SODA.
   
**dropSodaCollection.sql**
 - A SQL script to drop the SODA collection from the database.
