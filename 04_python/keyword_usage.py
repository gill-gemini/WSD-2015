#!/usr/bin/python

#def function keyword_usage():
	

def keyword_usage( text,seq):
	k=0
	tup1 =();
	words = text.split()
	print(words)
	for i in range(0,len(seq)):
		for j in range (0, len(words)):
			if(seq[i]==words[j]):
				if(k==0):
					tup1 += (True,)
					k=1
		if(k==0):
			tup1 +=(False,)
		k=0	
	#print(tup1)
	return tup1

# lets check the function	
#seq = ['abc123', 'into', 'ghi789']
#text = ('Dive into python')
#words = text.split()

#keyword_usage(seq ,text)
	

