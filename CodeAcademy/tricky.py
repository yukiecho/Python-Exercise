
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
