# Username
usrnm="scott"
# Password
psswd="<my password>"
# Data Source Name
dsn= """(DESCRIPTION =
     (ADDRESS = (PROTOCOL = TCP)(HOST = host.localdomain)(PORT = 1521))
     (CONNECT_DATA =
     (SERVER = DEDICATED)
     (SERVICE_NAME = pdb1.localdomain)))"""
#
# This file is updated in the third blog post.  The contents below are for that post - Connecting to the Autonomous JSON Database:
#
import os
os.environ['TNS_ADMIN'] = '/home/oracle/Python_Demo/Wallet_AJDBSEANS'

# Username
usrnm="scott"
# Password
psswd="<my password>"
# Data Source Name
dsn= "ajdbseans_tp"
