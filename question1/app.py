#!/usr/bin/env python3
def main():
	t = 'abcaabababaabaca'
	p = 'abcdabca'
	kmpMatch(t,p)

def kmpMatch(t, p):
	m = len(p)
	n = len(t)
	prefix = prefixFn(p)
	matches = []
	k = 0
        for i in range(n):
		while k>0 and T[i]!=P[k]:
			k = prefix[k-1]
		if t[i]==p[k]:
			k += 1
		if j==m:
			matches.append(i-(k-1))
			k = 0    
	return matches
	

def prefixFn(p):
	m = len(p)
	prefix = [0]*m
	k = 0

	for q in range (1, m):
		while k>0 and (p[k]!=p[q]):
			k = prefix[k]
		if p[k]==p[q]:
			k+=1
		prefix[q]=k
	print(p,prefix)
	return prefix

if __name__=='__main__':
	main()
