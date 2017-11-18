#!/usr/bin/python
# example xfinity wifi password: fever7538harbor


print("Creating temp list... Stand by.")
templist = open("temp.txt", "w")

with open("wordlists/5-letter-words.txt") as fivelist:
	with open("wordlists/numbers.txt") as numblist:
		flist = fivelist.readlines()
		nlist = numblist.readlines()
		for fword in flist:
			for numb in nlist:
				comb = fword.strip() + numb.strip() + "\n"
				templist.write(comb)
fivelist.close()
numblist.close()
templist.close()
print("\tdone")

print("Creating final keyspace... Grab a coffee.")
keyspace = open("keyspace.txt", "w")
with open("temp.txt") as templist:
	with open("wordlists/6-letter-words.txt") as sixlist:
		tlist = templist.readlines()
		slist = sixlist.readlines()
		for tword in tlist:
			for sword in slist:
				comb = tword.strip() + sword.strip() + "\n"
				keyspace.write(comb)
templist.close()
sixlist.close()
keyspace.close()
os.remove("temp.txt")  
print("\tdone")
