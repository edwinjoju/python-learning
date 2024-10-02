tweet = input("Enter tweet: ")
if(len(tweet)>140):
    print(f'{len(tweet)} characters is to long...')
else:
    print(f'{len(tweet)} characters will work')