#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pvaccess import *


def demonstrate_scalars():
	"""
	demonstrates how to operate on scalars in epics records

	performs puts and gets to observe writing data to records,
	then printing the new value after retrieving it.
	"""

	print('\nScalar Gets and Puts to EPICS pvRecord\n')

	channel = Channel('pvUByte')

	# Request the entire structure.
	pv = channel.get('field()')

	print pv

	# Access the fields of 'pv', pv is accessed just like a dictionary
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


def demonstrate_arrays():
	"""
	demonstrates how to operate on arrays in epics records.

	performs puts and gets to observe writing data to records,
	then printing the new values after retrieving them.
	"""

	print('\nArray Gets and Puts to EPICS pvRecord\n')
	
	channel = Channel('pvStringArray')
	
	pv = channel.get('field()')

	# Print the entire structure
	print pv
	
	# Write the array (just a list. Note that you can alternatively use numpy arrays.) 
	# See http://epics-pvdata.sourceforge.net/docbuild/pvaPy/tip/pvaccess.html#pvaccess.PvObject for more info on using numpy arrays
	
	# It's important to note here that if you first write a list of 5 items, and then write a list of 2 items, an exception will be
	# thrown. This is due to the partial update of an array not being implemented. If you write a list of 1 item, and then a list of
	# 2 items, no exception will be thrown. The error only occurs when making partial updates. Overwritting lists of smaller size
	# does not cause an error.

	channel.put(["What's the meaning of life?", "Not asking stupid questions."])

	# ERROR
	# channel.put(["blah"])

	# Retrieve the string array
	pv = channel.get('field(value)')
	strings = pv['value']
	for string in strings:
		print string


def demonstrate_nt_table():
	
	print('\nNTTable Gets and Puts to EPICS pvRecord\n')
	
	channel = Channel("pvNTTable")

	# Retrieve the entire structure
	pv = channel.get('field()')

	# pv is currently a PvObject. To use the NTTable convenience methods, we need an NTTable.
	table = NtTable(pv)

	labels = table.getLabels()
	col0 = table.getColumn(0)
	col1 = table.getColumn(1)
	col2 = table.getColumn(2)
	col3 = table.getColumn(3)

	# Print the column labels
	for label in labels:
		print '{0:>7}'.format(label),
	print '\n'

	# Print the column contents row by row.
	for val0, val1, val2, val3 in zip(col0, col1, col2, col3):
		print '{0:>7} {1:>7} {2:>7} {3:>7}'.format(val0, val1, val2, val3)


def main():

	demonstrate_scalars()

	demonstrate_arrays()

	demonstrate_nt_table()


if __name__ == '__main__':
	main()
