#!/usr/bin/env python3
import sys

def main(argv):
	if len(argv) != 4:
		print("ERROR: Missing command line arguments!")
		print("Usage: ./app.py text_file.txt pattern_file.txt output_file.txt")
		return 1
	try:
		textFile = open(argv[1], 'r')
		patternFile = open(argv[2], 'r')
	except IOError:
		print("ERROR: Missing input files!")
		return 2
	try:
		outputFile = open(argv[3], 'w+')
	except IOError:
		print("ERROR: Couldn't write into output file!")
		return 3
	
	text, pattern = textFile.readline().strip('\n '), patternFile.readline().strip('\n ')
	text_length, pattern_length = len(text), len(pattern)
	#n, m = len(t), len(p)
	for i in range(text_length-pattern_length+1):
		j = 0
		for j in range(pattern_length):
			if text[i+j] != pattern[j] and pattern[j] != '_':
				j -= 1
				break
		if (j == pattern_length-1):
			outputFile.write('{} '.format(i))

if __name__=='__main__':
	main(sys.argv)