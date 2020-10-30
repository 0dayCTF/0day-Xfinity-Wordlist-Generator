#!/usr/bin/python
# example xfinity wifi password: harbor7538fever
import os

print("Creating temp list... Stand by.")
templist = open("temp.txt", "w")

with open("wordlists/6list.txt") as sixlist:
	with open("wordlists/numbers.txt") as numblist:
		slist = sixlist.readlines()
		nlist = numblist.readlines()
		for fword in slist:
			for numb in nlist:
				comb = fword.strip() + numb.strip() + "\n"
				templist.write(comb)
sixlist.close()
numblist.close()
templist.close()
print("\tdone")

print("Creating final keyspace... Grab a beer!")
keyspace = open("keyspace6letter.txt", "w")
with open("temp.txt") as templist:
	with open("wordlists/5list.txt") as fivelist:
		tlist = templist.readlines()
		flist = fivelist.readlines()
		for tword in tlist:
			for sword in flist:
				comb = tword.strip() + sword.strip() + "\n"
				keyspace.write(comb)
templist.close()
fivelist.close()
keyspace.close()
os.remove("temp.txt")  
print("\tdone")
