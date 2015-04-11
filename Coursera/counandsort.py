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
