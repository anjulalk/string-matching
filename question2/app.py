#!/usr/bin/env python3
def main():
    #open DNA database and query base files
    try:
        dnaDatabaseFile = open('DNA Database.txt', 'r')
        queryBaseFile = open('querybase.txt', 'r')
    except IOError:
        print("ERROR: 'DNA Database.txt or 'querybase.txt' files doesn't exist!")
        return 1
    
    #open output text file
    try:
        outputFile = open('output.txt', 'w+')
    except IOError:
        print("ERROR: Can't write to 'output.txt' file!")
        return 2

    #genereate dnaDatabase and queryBase dictionaries
    #from dnaDatabaseFile and queryBaseFile text files
    #keys are descriptions and values are the actual strings
    dnaDatabase, queryBase = populateDict(dnaDatabaseFile), populateDict(queryBaseFile)

    #iterate over dnaDatabase
    for a,b in dnaDatabase.items():
        outputFile.write("{}\n".format(a))
        
        #detect if there was a match
        #if there was at least one match
        #should not output 'NOT FOUND'
        switch = False 
        
        #iterate over queryBase
        for m,n in queryBase.items():
            #get the index which the pattern matches
            match = kmpFn(b, n)
            if match!=-1:
                #at least one matche is found. flip!
                #will not print 'NOT FOUND' at the end
                switch = True
                outputFile.write("[{}] at offset {}\n".format(n, match)) #only output first occurence
        if switch==False:
            #means no matches found 
            outputFile.write('NOT FOUND\n')
        outputFile.write('\n')
    outputFile.close()

def populateDict(file):
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
    #returns the first index which the pattern matches
    #else returns -1
	n, m = len(t), len(p)
	k = 0
	prefix = prefixFn(p)

	for i in range(n):
		while k>0 and t[i]!=p[k]:
			k = prefix[k-1]
		if t[i]==p[k]:
			k += 1
		if k==m:
			return(i-(k-1))
	return -1

def prefixFn(p):
    #generates prefix list for kmpFn
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