fivelist = open("5list.txt", "w")
sixlist = open("6list.txt", "w")

with open("4000-common.txt") as common:
	clist = common.readlines()
	for cword in clist:
		cword = cword.strip()
		cword = cword.lower()
		if len(cword) == 5:
			cword = cword + "\n"
			fivelist.write(cword)
		elif len(cword) == 6:
			cword = cword + "\n"
			sixlist.write(cword)
		else:
			pass
fivelist.close()
sixlist.close()