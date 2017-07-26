#! /usr/bin/env python

import sys
from pvaccess import *

# Prints usage information and exits
def _help():
	print 'usage: database [-v / -h]'
	print '\t-v : verbose. prints record names.'
	print '\t-h : help. prints help information.'
	sys.exit(0)

# Instantiates and initializes a PvObject that conforms to the definition of a normative type scalar structure.
def ntScalar(scalar_type):

	pv = PvObject(
		{'value'     : scalar_type,		# Add a field of the specified type, name the field 'value'
		 'alarm'     : PvAlarm(),		# Add an alarm structure, name the field 'alarm'
		 'timeStamp' : PvTimeStamp()},	# Add a timestamp structure, name the field 'timeStamp'
		 'epics:nt/NTScalar:1.0')		# Name the structure.

	return pv

def main():

	if '-h' in sys.argv:
		_help()

	pvaServer = PvaServer()

	# Create an ntScalar of type 'double'
	pvaServer.addRecord('pvDouble', ntScalar(DOUBLE))

	# Create an ntScalar of type 'int'
	pvaServer.addRecord('pvInt', ntScalar(INT))

	# Create an ntScalar of type 'boolean'
	pvaServer.addRecord('pvBoolean', ntScalar(BOOLEAN))

	# Create an ntScalar of type 'ubyte'
	pvaServer.addRecord('pvUByte', ntScalar(UBYTE))

	# Create an ntScalar of type 'string array'
	# Note that all that is required to define an array is encapsulating the type in brackets.
	pvaServer.addRecord('pvStringArray', ntScalar([STRING]))

	# Print the record names if '-v' is given
	if '-v' in sys.argv:
		record_names = pvaServer.getRecordNames()
		print record_names

	# Wait for user input to exit.
	while True:
		input_str = raw_input("type 'exit' to quit: ")
		if input_str == str('exit'):
			break

if __name__ == '__main__':
	main()
