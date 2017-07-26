#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pvaccess import *

def main():
	channel = Channel('pvUByte')

	# Request the entire structure.
	pv = channel.get('field()')

	print pv

	# Access the fields of 'pv'
	print 'value:', 	pv['value']
	print 'alarm:', 	pv['alarm']
	print 'timeStamp:', pv['timeStamp']

	# Write to the value field of 'pv'
	channel.put(32, 'field(value)')

	# Observe the changed value
	pv = channel.get('field(value)')

	print '\n', pv

	# Update the nested fields. 
						# Note, that '.' is used to denote subfields.
	channel.put(2, 'field(alarm.status)')
	channel.put(1, 'field(alarm.severity)')

	# Observe the changed values
	pv = channel.get('field(alarm)')

	print pv
	
if __name__ == '__main__':
	main()
