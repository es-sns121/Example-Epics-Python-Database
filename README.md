# Example EPICS v4 Database in Python

## database.py
	This application serves as an example of how to instantiate an EPICS v4 database
	and populate it with records that house normative type data structures.
	
## client.py
	This application serves as an example of how to read and write to fields of records
	hosted on an EPICS v4 database.

## Prerequisites

	- Valid build of EPICS v4, note that pvaPy **must** be built. As of this writing, 26/7/2017,
	EPICS v4 is at version 4.6.0.
	- Valid installation of python 2. These applications were written and run with version 2.6.
	
## Running
	- To run the database simply type 
		> python database.py
	- To run the client, first run the database, and then type in another terminal
		> python client.py
