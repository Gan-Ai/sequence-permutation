import sys
import random

f1= open(sys.argv[1])
f2= open(sys.argv[2], 'w')

for l1 in f1:
	if '>' in l1:
		f2.write( l1 )
	if '>' not in l1:
		l=l1.strip()
		ls=list(l)
		random.shuffle(ls)
		l2=("".join(ls))
		f2.write( l2+'\n' )

f1.close()
f2.close()
