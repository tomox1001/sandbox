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
for line in open('response-time.log', 'r'):
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
		counts.update({lines[5]:1})
	
	# medians
	if lines[5] in medians:
		medians[lines[5]].insert(1,(int(lines[6])))
	else:
		medians.update({lines[5]:[int(lines[6])]})

print '############## total time'
for key, value in sorted(methods.items(), key=lambda x:x[1], reverse=True):
	print key + ',' + str(value)

print ''
print '############## call count'
for key, value in sorted(counts.items(), key=lambda x:x[1], reverse=True):
	print key + ',' + str(value)

print ''
print '############## time medians'
for key, value in sorted(medians.items()):
    medians[key] = getMedian(value)
for key, value in sorted(medians.items(), key=lambda x:x[1], reverse=True):
	print key + ',' + str(value)
