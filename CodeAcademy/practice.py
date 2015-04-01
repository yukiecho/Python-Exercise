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
