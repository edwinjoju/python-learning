#def laugh():
#    print("HA! "*10)
#laugh()

#printdef laugh(intensity):
#    print("HA"*intensity)
#laugh(10)


#def divide(x,y):
#    print(x/y)
#divide(10,2)

#def add(x,y):
#    return x+y
#num=add(10,5)
#print(num)

#def is_even(x):
#    if x%2==0:
#        return True
#    return False
#print(is_even(11))

#def sluggify(word):
#    return word.replace(" ","-")
#word= "Grandmas chicken salad"
#word = sluggify(word).lower()
#print(word)

#def count_vowels(word):
#    count=0
#    for x in word:
#        if x in "aieou":    
#            count+=1
#    return count
#word="pineapple"
#word=count_vowels(word)
#print(word)


def get_total( price, qty=1, tax=.02, discount=0):
    subtotal = price*qty*(1-discount)
    print(subtotal * (1+tax))


get_total(4.99,5,0.015,0.2)
get_total(price=9.75,qty=5,tax=0.01,discount=0.5)








