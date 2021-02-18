#!/usr/bin/python

import string

link = '<Download_Link_Prefix>_03_<Download_Link_Suffix>.mkv'
n = 10

file = open("links.txt","w")

while n < 14:
	new_link = link.replace("03",str(n))
	n+=1
	file.write(new_link)
	file.write('\n')
	print(new_link)


file.close()
