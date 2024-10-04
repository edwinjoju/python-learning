#task =["apple", "orange", "grapes", "mango"]
#print(task)
#print(task[0])
#print(task[0:4])

#list("hello")
#print(list('hello'))

#names = ["edwin", "delwin", "angel"]
#names[1]="athen"
#names.append("delwin")
#print(names)

#names.extend(task)
#print(names)

#names.insert(0,"dumbass")
#print(names)

#mark = [10,20,30,40,50,60]
#print(mark)
#mark.remove(20)
#print(mark)
#mark.pop()
#print(mark)
#mark.clear()
#print(mark)


#lang = ["python", "java", "C", "rust"]
#for x in lang:
#    print(x)

mark = [45,32,42,24,35,29,44,12,29]

tot=0
for x in mark:
    tot=tot+x
print(tot)
avg=tot/len(mark)

print(avg)