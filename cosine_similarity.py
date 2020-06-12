#!/local/bin/python3
from nltk.tokenize import word_tokenize
import math
import sys

#print(sys.argv)

test = sys.argv[1]
file1 = sys.argv[2]
file2 = sys.argv[3]

f = open(test , "r")
file1 = open(file1 , "r")
file2 = open(file2 , "r")
word_list = [i.strip().lower() for i in f]


v1 = {}
v2 = {}
for j in file1:
	temp_list = word_tokenize(j)
	for i in temp_list:
		i = i.lower()
		if i in v1:
			v1[i]=v1[i]+1
		elif i in word_list:
			v1[i] = 1

for j in file2:
        temp_list = word_tokenize(j)
        for i in temp_list:
                i = i.lower()
                if i in v2:
                        v2[i]=v2[i]+1
                elif i in word_list:
                        v2[i] = 1

numerator = 0
for i in v1:
	if i in v2:
		numerator = numerator + (v1[i] * v2[i])
d1=0
d2=0

for j in v1:
	d1 = d1 + v1[j]*v1[j]
for j in v2:
        d2 = d2 + v2[j]*v2[j]

denominator = d1*d2
denominator = math.sqrt(denominator)

#print(numerator)
#print(denominator)

if denominator == 0:
	print("Cosine similarity not defined! (Division by zero!)")
else:
	answer = numerator/denominator
	print(answer)


f.close()
file1.close()
file2.close()
