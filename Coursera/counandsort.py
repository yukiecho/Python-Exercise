#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.



name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
ls = []
counts = {}

for line in handle:
	if line.startswith("From "):
		lls = line.split()
		ls.append(lls[5][0]+lls[5][1])

for time in ls:
	counts[time] = counts.get(time,0)+1
        
for k,v in sorted(counts.items()):
    print k,v
