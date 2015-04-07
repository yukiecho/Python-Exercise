list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b

# A function to check whether a number is interger or not. The principal behind is that whether the difference between round number and original number is equal to 0 or not




# sum all the digits up
def digit_sum(n):
    num_list = []
    while n - n%10 != 0:
        num_list.append(n%10)
        n = (n - n%10)/10
    else: num_list.append(n)
    
    su = 0
    for a in num_list:
        su = a + su
        
    return su
#For example: anti_vowel("Hey You!") should return "Hy Y!".
def anti_vowel(text):
    vowel = "aeiouAEIOU"
    tem = []
    for t in text:
        if t in vowel: pass
        else: tem.append(t)
        
    return "".join(tem)


#Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [ x for x in range(1,16) if (x%3 ==0 or x%5==0)]

print threes_and_fives


#
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

nessage = ["N"]*len(garbled)

for n in range(0,len(garbled)):
    nessage[n] = garbled[len(garbled)-1-n]
 
m = 0   
message = ["N"] * int(len(nessage)/2+1)
for n in range(0,47):
    if nessage[n] == "X":
        continue
    else:
        message[m] = nessage[n]
        m +=1
print "".join(message)

#another way
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

#bitmove practice
#Flip the nth bit (with the ones bit being the first bit) and store it in result.
def flip_bit(number,n):
    mask = (0b1 <<(n-1))
    desired = number ^ mask
    return bin(desired)
