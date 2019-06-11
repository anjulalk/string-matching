#!/usr/bin/env python3
def main():
	t = 'aabcdefabcd'
	p = 'a_c'

	Q = {}
	q = p.strip().split('_')
	k = len(q)
	for i in range(k):
		_p = q[i]
		Q[_p] = kmpMatch(t, _p)

	for i in range(k):
		p = q[i]
		occ = Q[p]
		for j in occ:
			n = j+len(p)
			print(q[i+1], n)
	print(Q)
	
		
		
		
def kmpMatch(t, p):
	m = len(p)
	n = len(t)
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
	print(t,p, matches)	
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
	return prefix

if __name__=='__main__':
	main()
