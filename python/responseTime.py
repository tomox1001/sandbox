#!/usr/bin/env python

def getMedian(numericValues):
  theValues = sorted(numericValues)
  if len(theValues) % 2 == 1:
    return theValues[(len(theValues)+1)/2-1]
  else:
    lower = theValues[len(theValues)/2-1]
    upper = theValues[len(theValues)/2]
    return (float(lower + upper)) / 2  

methods = {}
counts = {}
medians = {}
for line in open('responseMain', 'r'):
#for line in open('responsetest', 'r'):
	lines = line.split(' ')
	# methods
	if lines[5] in methods:
		methods[lines[5]] = int(methods[lines[5]]) + int(lines[6])
	else:
		methods.update({lines[5]:lines[6]})

	# counts
	if lines[5] in counts:
		counts[lines[5]] = int(counts[lines[5]]) + 1
	else:
		counts.update({lines[5]:0})
	
	# medians
	if lines[5] in medians:
		medians[lines[5]].insert(1,(int(lines[6])))
	else:
		medians.update({lines[5]:[int(lines[6])]})

print '############## methods'
for key, value in sorted(methods.items()):
	print key + ',' + str(value)
print '############## counts'
for key, value in sorted(counts.items()):
	print key + ',' + str(value)
print '############## medians'
for key, value in sorted(medians.items()):
	print key + ',' + str(getMedian(value))
