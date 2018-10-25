newlist = open("6letters.txt", "w")

with open("6-letters.txt") as fivelist:
	flist = fivelist.readlines()
	for fword in flist:
		fword = fword.strip()
		if fword.endswith("s"):
			pass
		elif fword.endswith("ed"):
			pass
		elif fword.endswith("er"):
			pass
		elif fword.endswith("y"):
			pass
		else:
			word = fword + "\n"
			newlist.write(word)
fivelist.close()
newlist.close()
