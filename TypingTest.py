from time import time
import random

wordList = ['crocodile', 'pencil', 'sanitize', 'Canada', 'controller', 'highway', 'cookie', 'jacket', 'invention', 'procrastinate', 'microscopic', 'synergy', 'Tunisia', 'blossom', 'battleship', 'aeronautics', 'scissors', 'Manilla', 'obsidian', 'Saturn', 'Mozambique', 'triathlon', 'personalize', 'unyielding', 'denture', 'familiarity', 'electricity',]
sentenceList = ['Get me out of here!', 'He picked up his pencil and started writing.', 'Please sanitize your hands.', 'Man, I love frogs.', 'You cannot pass!', 'I did it my way.', "There's a drive into deep left field by Castellanos,", 'The creatures outside looked from pig to man, and from man to pig, and from pig to man again;', 'What are men to rocks and mountains?', 'Release the Kraken!', 'Somewhere over the rainbow,']

randomword1 = (random.choice(wordList))
randomword2 = (random.choice(wordList))
randomword3 = (random.choice(wordList))

randomsentence = (random.choice(sentenceList))

def timeElapsed(stime, etime):
    time = etime - stime

    return time

def TypeTest():
        
    print("Hello, and welcome to my Python typing test!\n \nFor the test, you have two options. Test your speed by typing three words or by typing one sentence.\n \nWell now, the choice is yours, have fun!\n")
    choice = input('"Words" or "Sentence" ?: ')
    if str(choice) == 'Words':
        ContinueWords()
    elif str(choice) == 'Sentence':
        ContinueSentence()
    else:
        print('\nPlease try again, you spelled one of the choices wrong.\n')
        TypeTest()
    
def ContinueWords():
    print('\nYour words are:\n')
    print(randomword1)
    print(randomword2)
    print(randomword3)
    print('\nRemember, capitalization matters!')
    input('Press the enter key when you are ready.')
    print('\nGo!')
    
    wordstarttime = time()
    
    wordOne = input('First word: \n')
    print(wordOne)
    wordTwo = input('Second word: \n')
    print(wordTwo)
    wordThree = input('Third word: \n')
    print(wordThree)
    
    wordendtime = time()
    
    if wordOne == randomword1:
        print('Correct! Your first word was: ' + (randomword1) + '\nYou entered: ' + wordOne)
    else:
        print('Incorrect! Your first word was: ' + (randomword1) + '\nYou entered: ' + wordOne)
        
    if wordTwo == randomword2:
        print('\nCorrect! Your first word was: ' + (randomword2) + '\nYou entered: ' + wordTwo)
    else:
        print('\nIncorrect! Your first word was: ' + (randomword2) + '\nYou entered: ' + wordTwo)
        
    if wordThree == randomword3:
        print('\nCorrect! Your first word was: ' + (randomword3) + '\nYou entered: ' + wordThree)
        print('\nYour time was: ' + str(timeElapsed(wordstarttime, wordendtime)))
    else:
        print('\nIncorrect! Your first word was: ' + (randomword3) + '\nYou entered: ' + wordThree)
        print('\nYour time was: ' + str(timeElapsed(wordstarttime, wordendtime)))
        
    print('========== Thank you for playing! ==========')
    
    playagain = input('Play again? [Y/N] ?: ')
    print(playagain)
    
    if playagain == 'Y':
        TypeTest()
    else:
        print('\nBYE')

def ContinueSentence():
    print('You have chosen: "Sentence".\n \nFor this task you will have to type out one random sentence from the list.\n \nAs you can see, the difficulty of the sentences vary.\n \nIncluded in the list are sentence fragments, so not every item ends in a question mark, exclamation point, or period. \n \nThe timer will start after you input something \n \nREMEMBER, punctuation capitalization matter, so be careful!\n')
    print('Here is your sentence: ' + randomsentence)
    input('Press the enter key when you are ready: ')
    print('\nGo!')
    
    sentencestarttime = time()
    

    sentence = input('\nYour sentence: ')
    print(sentence)
    
    sentenceendtime = time()
    
    if sentence == randomsentence:
        print('\nCorrect! Your sentence was: ' + (randomsentence) + '\nYou entered: ' + sentence)
        print('\nYour time was: ' + str(timeElapsed(sentencestarttime, sentenceendtime)))
    else:
        print('\nIncorrect! Your sentence was: ' + (randomsentence) + '\nYou entered: ' + sentence)
        print('\nYour time was: ' + str(timeElapsed(sentencestarttime, sentenceendtime)))
        
    print('========== Thank you for playing! ==========')
    
    playagain = input('Play again? [Y/N] ?: ')
    print(playagain)
    
    if playagain == 'Y':
        TypeTest()
    else:
        print('\nBYE')
TypeTest()