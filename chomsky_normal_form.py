
# lines=[]
# while 1:
# 	try:
# 		line = input()
# 	except EOFError:
# 		break
# 	lines.append(line.strip())
# s = " ".join(lines)

#pos_tags=['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP','S', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
s="(S (WNP (WDT What) (NN courses)) (VP (BE are) (VP (VBN offered) (PP (IN in) (NN fall))))) (S (WNP Who) (VP (VBZ teaches) (NP (NN CSCI) (NN 1100)))) (S (WNP (WDT (WRB How) (JJ many)) (NN students)) (VP (BE are) (VB (VBG taking) (NP (NN CSCI) (NN 1108)))))"
tokens = []

lis = s.split(" ")
for i in lis:
	word=""
	for j in i:
		if j=="(":
			tokens.append(j)
		elif j!=")":
			word+=j
		elif j==")":
			tokens.append(j)
		tokens.append(word)
	# for k in i:
	# 	if k == ")":
	# 		tokens.append(k)
print(tokens)
bracks=[]
for i in tokens:
	if i == "(" or i == ")":
		bracks.append(i)


def check_gram(Hash): 
	try:
		if Hash[-1] == 1 and Hash[-2] == 1 and Hash[-3] == 0:
			return 1
		return 0
	except:
		print("")


flag=0
stack = []
Hash = []
for i in bracks:
	if i=="(":
		stack.append(i)
		Hash.append(0)
	else:
		# print(str(len(stack)) + " s " + str(len(Hash)))
		if len(stack)==1 and len(Hash)==1:
			# print("ausdiausd")
			Hash.pop()
			stack.pop()
			# print("ahoy")
		else:
			# print("gg")
			stack.pop()
			Hash[-1]+=1
			check = check_gram(Hash)
			if check == 1:
				Hash.pop()
				Hash.pop()

	# print(stack)
	# print(Hash)

if len(Hash) == 0:
	flag = 0
else:
	flag = 1


if flag==1:
	print("Not valid CNF trees.\n")
else:
	print("Valid CNF trees.\n")
# 	if i in pos_tags and stack[-1]=="(":
# 		stack.append(i)

# print(stack)





