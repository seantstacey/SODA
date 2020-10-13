# SODA
Sample Python scripts to demonstrate SODA

This repo provides sample code to supplement a 3 part series from the blog site: https://seanstacey.org/?page_id=261

Part One of the Blog covers the basics of connecting a Python program to an Oracle database using cx_Oracle.  The following scripts are used in Part One.

**MyConnectInfo.py**
 - This script holds the login credentials to connect to the Oracle Database.
   
**step-one.py**
 - This script demonstrates connecting from Python to Oracle using the cx_Oracle module and then querying a relational table to print the rows in Python.
 
**step-two.py**
 - This script builds upon the step-one.py script. It uses the MyConnectInfo.py to connect to the Oracle database.
 
 **step-three.py**
 - This script demonstrates creating an Oracle table that contains a JSON Document.  It then performs a SQL insert into the table including a JSON entry. The data is then queried using two different approaches.
