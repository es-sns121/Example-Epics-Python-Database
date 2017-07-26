#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pvaccess import *

def main():
	channel = Channel('pvUByte')

	# Request the entire structure.
	pv = channel.get('field()')

	print pv

	# Access the fields of 'pv', pv is just a dict
	print '    value:', pv['value']
	print '    alarm:', pv['alarm']
	print 'timeStamp:', pv['timeStamp']

	# Write to the value field of 'pv'
	# All numeric writes work like this. For boolean just replace the number with True or False
	# For strings, just pass the string you want to be written as the first argument.
	channel.put(32, 'field(value)')

	# Observe the changed value
	pv = channel.get('field()')

	print '\n', pv

	# Update the nested fields. 
	# Note that '.' is used to denote subfields.
	# For example field(field.subfield.subfield_of_subfield) This pattern continues as deep as the structure goes.
	channel.put(2, 'field(alarm.status)')
	channel.put(1, 'field(alarm.severity)')

	# Observe the changed values
	pv = channel.get('field(alarm)')

	print pv
	
## Handling Arrays
	channel = Channel('pvStringArray')
	
	pv = channel.get('field()')

	# Print the entire structure
	print pv
	
	# Write the array (just a list. Note that you can alternatively use numpy arrays.) 
	# See http://epics-pvdata.sourceforge.net/docbuild/pvaPy/tip/pvaccess.html#pvaccess.PvObject for more info on using numpy arrays
	
	# It's important to note here that if you first write a list of 5 items, and then write a list of 2 items, an exception will be
	# thrown. This is due to the partial update of an array not being implemented. If you write a list of 1 item, and then a list of
	# 2 items, no exception will be thrown. The error only occurs when making partial updates, overwritting lists of smaller size
	# does not cause error.

	channel.put(["What's the meaning of life?", "Not asking stupid questions."])

	# ERROR
	# channel.put(["blah"])

	# Retrieve the string array
	pv = channel.get('field(value)')
	strings = pv['value']
	for string in strings:
		print string

if __name__ == '__main__':
	main()
