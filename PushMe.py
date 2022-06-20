#I get pushed regularly!
import random

#1. create txt file 
#2. write a function which writes into this file when called
#3. run script and run autopush to see if it works

def pushMe():
    #create rare number for 
    randomNumber = random.randint(0, 100000) + random.randint(0, 100000) - random.randint(0, 100000) * random.randint(0, 100000) / random.randint(0, 100000)
    return str(randomNumber)

def writeToFile():
    with open("Change.txt", "w") as textFile:
        textFile.write(pushMe())

writeToFile()