#Knights to was "ni" video reference
#https://www.youtube.com/watch?v=zIV4poUZAQo

file = open("stop-words.txt")
stopwords = file.readlines()

#import wikipedia
#print wikipedia.summary("Wikipedia")

def removeStopwords(input):
    input = " " + input + " "
    for word in stopwords:
        next = word.strip()
        input = input.replace(" " + next + " ", " ")
        input = input.replace(" called ", " ")
        input = input.replace(" name ", " ")
        input = input.replace(" thank ", " ")
        input = input.replace(" thanks ", " ")
    input = input.strip()
    return input


while True:
    input = raw_input("Hello, what is your name?")
    greeting = input
    greeting = removeStopwords(greeting)
    input = raw_input("Hi %s, How are you today?" % greeting)
    reply = input
    reply = removeStopwords(reply)
    input = raw_input("%s, me too! :), where are you at the moment?" % reply)
    question = input
    question = removeStopwords(question)
    input = raw_input("%s, I was there many years ago! What would you like to know about?" % question)
    quirk = input
    quirk = removeStopwords(quirk)
    input = raw_input("%s? Here are some facts about %s:" % quirk)
    #fact = 
    
    print(input)
    
    
    #hello what is your name ? My name is bob
#Hiya bob, what you doing today ? Work
#Work ! That sucks

#file = open("stop-words.txt")
#stopwords = file.readlines()


#while True:
#    input greeting()
#    for word in stopwords:
#        next = word.strip()
#        input = input.replace(" " + next + " ", " ")
#        input = input.replace(" called ", " ")
#        input = input.replace(" name ", " ")
#    greeting = raw_input("Hello, what is your name?")
#    reply = raw_input("Hi %s, How are you today?" % greeting)
#    question = raw_input("%s, me too! :), where are you at the moment?" % reply)
#    quirk = raw_input("%s, I was there many years ago!" % question)

#if len(greeting) > 0 and greeting.isalpha():
#    print(raw_input.reply)
#if len(reply) > 0 and reply.isalpha():
#    print(raw_input.question)
#if len(question) > 0 and question.isalpha():
#    print(raw_input.quirk)
        
    
    
    