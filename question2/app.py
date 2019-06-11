#!/usr/bin/env python3
def main():
    dnaDBFile = open('DNA Database.txt', 'r')
    dnaDB = {}

    #populate dnaDB dictionary from dnaDBFile text file
    for line in dnaDBFile:
        global desc
        if line[0]=='>':
            desc = line.strip('>\n')
            if desc != 'EOF':
                dnaDB[desc] = ''
        else:
            dnaDB[desc] = dnaDB[desc] + line.strip('\n ')
    
    queryDBFile = open('querybase.txt', 'r')
    queryDB = {}
    #populate queryDB dictionary from queryDBFile text file
    for line in queryDBFile:
        global qdesc
        if line[0]=='>':
            qdesc = line.strip('>\n')
            if qdesc != 'EOF':
                queryDB[qdesc] = ''
        else:
            queryDB[qdesc] = queryDB[qdesc] + line.strip('\n ')
    
    for a,b in dnaDB.items():
        print(a)
        for m,n in queryDB.items():
            matches = kmpMatch(b, n)
            if len(matches)==0:
                print('NOT FOUND')
            else:
                print('[' + n + '] at offset ', end='')
                for match in matches:
                    print(match, end=' ')
                print()

def kmpMatch(t, p):
	n = len(t)
	m = len(p)
	prefix = prefixFn(p)
	matches = []
	k = 0
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
