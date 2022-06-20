#I get pushed regularly!
import random

def pushMe():
    #create rare number for 
    randomNumber = random.randint(0, 100000) + random.randint(0, 100000) - random.randint(0, 100000) * random.randint(0, 100000) / random.randint(0, 100000)
    return randomNumber 

pushMe()