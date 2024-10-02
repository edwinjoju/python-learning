
#  ----------
#    PART 1
#  ----------
#word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
#for n in word:
#    print(n)

# Write a while loop that does the same thing!
#n = len(word)
#while n !=0:
#    print(word[n-1])
#    n=n-1


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
#n=100
#while(n<141):
#    print(n)
#    n+=2


# Write a for loop that does the same thing (with range())
#for x in range(100,141,2):
#    print(x)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

user = input("Enter the passphrase: ")
while user!="sillygoose":
    user = input("Enter the passphrase: ")
else:
    print("Correct u can proceed...")