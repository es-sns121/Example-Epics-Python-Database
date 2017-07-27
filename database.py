#! /usr/bin/env python

from sys import argv, exit
from pvaccess import *

# Prints usage information and exits
def _help():
	
	print 'usage: database [-v / -h]'
	print '\t-v : verbose. prints record names.'
	print '\t-h : help. prints help information.'
	exit(0)


# Instantiates and initializes a PvObject that conforms to the definition of a normative type scalar structure.
def ntScalar(scalar_type):

	pv = PvObject(
		{'value'     : scalar_type,		# Add a field of the specified type, name the field 'value'
		 'alarm'     : PvAlarm(),		# Add an alarm structure, name the field 'alarm'
		 'timeStamp' : PvTimeStamp()},	# Add a timestamp structure, name the field 'timeStamp'
		 'epics:nt/NTScalar:1.0')		# Name the structure.

	return pv


# Adds scalar records to database
def add_scalar_records(pva_server):
	
	# Create an ntScalar of type 'double'
	pva_server.addRecord('pvDouble', ntScalar(DOUBLE))

	# Create an ntScalar of type 'int'
	pva_server.addRecord('pvInt', ntScalar(INT))

	# Create an ntScalar of type 'boolean'
	pva_server.addRecord('pvBoolean', ntScalar(BOOLEAN))

	# Create an ntScalar of type 'ubyte'
	pva_server.addRecord('pvUByte', ntScalar(UBYTE))

	# Create an ntScalar of type 'string array'
	# Note that all that is required to define an array is encapsulating the type in brackets.
	pva_server.addRecord('pvStringArray', ntScalar([STRING]))


# Adds an instance of NTTable to the database.
def add_nt_table(pva_server):

	# Table with four columns. Each column is an array of the respective type.
	table = NtTable([STRING, INT, DOUBLE, BOOLEAN])
	
	# Set the column names (labels)
	table.setLabels(['strings', 'ints', 'doubles', 'booleans'])

	pva_server.addRecord('pvNTTable', table)


def main():

	if '-h' in argv:
		_help()

	pva_server = PvaServer()

	add_scalar_records(pva_server)

	add_nt_table(pva_server)

	# Print the record names if '-v' is given
	if '-v' in argv:
		record_names = pva_server.getRecordNames()
		print record_names

	# Wait for user input to exit.
	while True:
		input_str = raw_input("type 'exit' to quit: ")
		if input_str == str('exit'):
			break


if __name__ == '__main__':
	main()
