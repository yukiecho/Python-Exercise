
# http://www.codecademy.com/courses/python-intermediate-en-rCQKw/1/4?curriculum_id=4f89dab3d788890003000096#
# http://stackoverflow.com/questions/19290762/cant-modify-list-elements-in-a-loop-python


 def censor(text,word):
    li = text.split()
    for w in range(len(li)):
        a = len(li[w])
        if li[w] == word:
            li[w] = "*" * len(li[w])
            print (li)
        else: pass
    return " ".join(li)
    
print censor("hey hey hey","hey")

# remove duplicate values in a list
def remove_duplicates(li):
    new_li = []
    if len(li)<=0:
        pass
    else:
        
        for w in range(len(li)-1):
            for n in range(w+1,len(li)):
                if li[w] == li[n]:
                    break
            else:new_li.append(li[w])
        if li[len(li)-1] not in new_li:
            new_li.append(li[len(li)-1])
            
    return new_li
    
   # find median
   # Last but not least, note that (2 + 3) / 2 is not the same as (2 + 3) / 2.0! The former is integer division, meaning  #Python will try to give you an integer back. You'll want a float, so something like (2 + 3) / 2.0 is the way to go.
   def median(ls):
    changdu = len(ls)/2
    ls = sorted(ls)
    print (ls)
    if len(ls)==1:
        me = ls[0]
    elif len(ls)%2!=0:
        me = ls[int(changdu)]
    else:
        me = (ls[int(changdu)]+ls[int(changdu)-1])/2.0
    return me
    
   # Exam scores statistics
   grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance = variance / len(scores)
    return variance

print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades)

print grades_std_deviation(variance)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(grades_variance(grades))

# Just print out even number
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
