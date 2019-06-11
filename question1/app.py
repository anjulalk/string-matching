#!/usr/bin/env python3
import sys

# Gets text, pattern and output file names as arguments
# Exit if missing arguments
def main(argv):
	# Check if all arguments exist
	if len(argv) != 4:
		print("ERROR: Missing command line arguments!")
		print("Usage: ./app.py text_file.txt pattern_file.txt output_file.txt")
		return 1
	
	# Try to open the files
	try:
		textFile, patternFile = open(argv[1], 'r'), open(argv[2], 'r')
	except IOError:
		print("ERROR: Missing input files!")
		return 2
	
	# Try to open output file
	# Exit if doesn't have permission to write
	try:
		outputFile = open(argv[3], 'w+')
	except IOError:
		print("ERROR: Couldn't write into output file!")
		return 3
	
	# Run the function to genereate outputFile
	patternMatch(textFile, patternFile, outputFile)

	# Close opened files
	textFile.close()
	patternFile.close()
	outputFile.close()

def patternMatch(textFile, patternFile, outputFile):
	# Get the contents of text and pattern files to respective string variables
	text, pattern = textFile.readline().strip('\n '), patternFile.readline().strip('\n ')
	text_length, pattern_length = len(text), len(pattern)
	
	# Iterate over the text
	for i in range(text_length-pattern_length+1):
		j = 0 # j is the position of the pattern which is matched
		for j in range(pattern_length): # Iterate over the pattern
			if text[i+j] != pattern[j] and pattern[j] != '_': 
				# MISMATCH!
				j -= 1 # Decrement j by one so the current character position is ignored
				break
		if (j == pattern_length-1): # Checks if pattern is complete
			outputFile.write('{} '.format(i))

if __name__=='__main__':
	main(sys.argv)