#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The #program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a #Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the #dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
ls = []
dic = dict()

for line in handle:
	if line.startswith("From "):
		lls = line.split()
		ls.append(lls[1])
      
for name in ls:
	if name not in dic:
		dic[name] = 1
	else:
		dic[name]+=1

maxi = 0
for name in dic:
	if dic[name] > maxi:
		maxi = dic[name]
		string = name
        
print "%s %d" %(string,maxi)

