#!/usr/bin/env python3
def main():
    #open database input files
    try:
        dnaDBFile = open('DNA Database.txt', 'r')
        queryDBFile = open('querybase.txt', 'r')
    except IOError:
        print("ERROR: Check if 'DNA Database.txt and 'querybase.txt' files exist!")
        return 1
    
    #open output text file
    try:
        outputFile = open('output.txt', 'w+')
    except IOError:
        print("ERROR: Could not write to 'output.txt' file!")
        return 2

    
    #populate dnaDB and queryDB dictionaries from dnaDBFile and queryDBFile text files
    #keys are descriptors and values are the actual strings
    dnaDB, queryDB = populateDB(dnaDBFile), populateDB(queryDBFile)

    #iterate over dnaDB
    for a,b in dnaDB.items():
        #print(a)
        outputFile.write("%s\n"%a)
        switch = False #detect if there was a match
        for m,n in queryDB.items():
            matches = kmpFn(b, n)
            if len(matches)!=0:
                #print('[' + n + '] at offset ', end='')
                outputFile.write("[%s] at offset"%n)
                for match in matches:
                    #print(match, end=' ')
                    outputFile.write(" %d"%match)
                    switch = True
                #print()
                outputFile.write('\n')
        if switch==False:
            #means no matches found 
            #print('NOT FOUND')
            outputFile.write('NOT FOUND\n')
        outputFile.write('\n')
    outputFile.close()

def populateDB(file):
    dict, desc = {}, ''
    for line in file:
        #check if line contains title
        if line[0]=='>':
            #retrieve the actual title
            desc = line.strip('>\n')
            if desc != 'EOF':
                #add to dictionary as key
                dict[desc] = ''
        else:
            #concatenate to the value of previously read key
            dict[desc] = dict[desc] + line.strip('\n ')
    return dict

def kmpFn(t, p):
	n, m = len(t), len(p)
	matches, k = [], 0
	prefix = prefixFn(p)

	for i in range(n):
		while k>0 and t[i]!=p[k]:
			k = prefix[k-1]
		if t[i]==p[k]:
			k += 1
		if k==m:
			matches.append(i-(k-1))
			k = prefix[k-1]
	return matches

def prefixFn(p):
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