from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Edwin")
engine.runAndWait()

statement = input("Enter your statement: ")
blob  = TextBlob(statement)
while blob.sentiment.polarity < 0.3:
    engine.say("Please be more positive")
    engine.runAndWait()
    statement= input(">")
    blob = TextBlob(statement)

engine.say("Thank you motherfucker, you fucking did it...")
engine.runAndWait()