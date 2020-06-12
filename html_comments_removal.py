#!/local/bin/python3
import sys
import re
# regex for html tags
tag_start = re.compile("<[^>]*>")

# regex for html comments
comm_start = re.compile("<!--(.)+-->|(?=<!--)([\s\S]*?)-->") 
inp = sys.stdin.read()

def comm(match_obj2):
	
	comm_tag = "<!--"
	commstr = match_obj2.group()[0:]
	print(commstr)
	for j in commstr[4:-3]:
		if(j=="\n"):
			comm_tag+="\n"
		else:
			comm_tag+="."
	comm_tag+="-->"
	# print("============="+comm_tag)
	return comm_tag


def tag(match_obj):
	tagstr = match_obj.group()[1:]
	#print(tagstr)
	normal_tag = "<"
	if(tagstr[0:3]=="!--"):
		normal_tag+=tagstr
		return normal_tag
	else:
		c=0
		l=len(tagstr)
		for char in tagstr:
			if(c<l-1):
				if(char=="\n"):
					normal_tag+="\n"
				else:
					normal_tag+="."

			c+=1
	normal_tag+=">"
	return normal_tag


comment = re.sub(comm_start,comm,inp)
tag_str = re.sub(tag_start, tag, comment)
print(tag_str)

# the regular expression for matching comments was taken from a stackoverflow answer. I have provided the appropriate citation below.

	# 					References
	# [1] E. Mihailescu, “RegExp to strip HTML comments,” Stack Overflow, 22-Mar-2015. [Online]. Available: https://stackoverflow.com/questions/1084741/regexp-to-strip-html-comments/29194283. [Accessed: 26 Feb 2020].