#!/usr/bin/env python3
def main():
	t = 'abx'
	p = 'a_b'
	
	n, m = len(t), len(p)
	for i in range(n-m+1):
		for j in range(0, m):
			if t[i+j] != p[j] and p[j] != '_':
				break
		if (j==m-1):
			print('found at', i)



if __name__=='__main__':
	main()
