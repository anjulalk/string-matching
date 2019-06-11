#!/usr/bin/env python3
def main():
    # Try to open DNA database and query base files
    try:
        dnaDatabaseFile, queryBaseFile = open('DNA Database.txt', 'r'), open('querybase.txt', 'r')
    except IOError:
        print("ERROR: 'DNA Database.txt or 'querybase.txt' files doesn't exist!")
        return 1
    
    # Try to open output text file
    try:
        outputFile = open('output.txt', 'w+')
    except IOError:
        print("ERROR: Can't write to 'output.txt' file!")
        return 2

    # Genereate dnaDatabase and queryBase dictionaries
    # from dnaDatabaseFile and queryBaseFile text files
    # Keys are the DNA descriptions and values are the actual DNA strings
    dnaDatabase, queryBase = generateDict(dnaDatabaseFile), generateDict(queryBaseFile)

    # Iterate over queryBase
    for a,b in queryBase.items():
        # Write the description of query
        outputFile.write("{}\n".format(a))
        
        # Detect if there was at lease one match
        # If there was at least one match
        # it should not write 'NOT FOUND'
        foundSwitch = False 
        
        # Iterate over dnaDatabase
        for m,n in dnaDatabase.items():
            # Get the index which the pattern first matches
            match = kmpFn(n, b)
            if match!=-1:
                # At least one match is found. FLIP!
                foundSwitch = True
                outputFile.write("[{}] at offset {}\n".format(m, match)) # Only output first occurence
        if foundSwitch==False:
            # Means no matches found 
            outputFile.write('NOT FOUND\n')
        outputFile.write('\n')
    outputFile.close()

# Generates a dictionary for easy retireval
# Key -> Title, Value -> DNA Sequence
def generateDict(file):
    dict, desc = {}, ''
    for line in file:
        # Check if line contains title
        if line[0]=='>':
            # Retrieve the actual title
            desc = line.strip('>\n ')
            if desc != 'EOF':
                # Add to dictionary as key
                dict[desc] = ''
        else:
            # Concatenate to the value of previously read key
            dict[desc] = dict[desc] + line.strip('\n ')
    return dict

def kmpFn(t, p):
    # Returns the first index which the pattern matches
    # Else returns -1
	n, m, k, prefix = len(t), len(p), 0, prefixFn(p)

	for i in range(n):
		while k>0 and t[i]!=p[k]:
			k = prefix[k-1]
		if t[i]==p[k]:
			k += 1
		if k==m:
			return(i-(k-1))
	return -1

def prefixFn(p):
    # Returns prefix table list for kmpFn
	m = len(p)
	prefix = [0]*m
	k = 0
	for q in range (1, m):
		while k>0 and (p[k]!=p[q]):
			k = prefix[k-1]
		if p[k]==p[q]:
			k+=1
		prefix[q]=k
	return prefix

if __name__=='__main__':
	main()