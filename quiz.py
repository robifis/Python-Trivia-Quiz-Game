#!/usr/bin/python3

# """
# GOAL: Create a Quiz Game that pulls data from an online API.(Multiple choice)
# TODO:
# 1) Get the API loaded correctly 
# 2) Display the data to the user
# 3) Count Score
# 4) Display Score after X number of questions
# 5) Play Again?
# """"

import requests, pprint, json, base64, random
from random import shuffle, sample

#CAT_URL = 'https://opentdb.com/api_category.php'

# Calling the game
def main ():

    print('Welcome to the Great Big Genereal knowledge Quiz!')


    #!  Getting Categories
    CAT_URL = 'https://opentdb.com/api_category.php'

    cat_res = requests.get(CAT_URL) 
    catDump = cat_res.json()

    # Printing Categories Out
    for i in range(23):
        print(str(i+1) + ' ' + catDump['trivia_categories'][i]['name']) 

    # User selects Category
    selected_category = int(input('Please select a Category (Enter a number between 1 and 23): '))   
    
    # Validating Category
    while selected_category not in range(1,23):
        selected_category = int(input('Please select a Category (Enter a number between 1 and 23): '))   
    else:
        # How many questions?
        q_nr = input('How many questions would you like?: ')

    cat_ID = selected_category + int(8)

    # QUIZ URL!
    QUIZ_URL = f'https://opentdb.com/api.php?category={cat_ID}&amount={q_nr}&type=multiple&encode=base64'

    # Calling the API and getting the data
    response = requests.get(QUIZ_URL)
    quizDump = response.json()

# Setting the score to '0'
    score = 0
   
    # Gettning all the questions printed out.
    # It's 10 because that's how many questions there are initially
    for i in range(int(q_nr)):
        print('==========================================================================')
        # This decodes the text into readable characters from base64 to utf-8 ==> Make sure to import base64!!
        q = quizDump['results'][i]['question']
        decodedQuestion = base64.b64decode(q).decode('utf-8')
        # Printing first Question
        print('Question '+ str(i+1))
        print(decodedQuestion)
        print('==========================================================================')
        
        
        # Empty list where the answers will be stored to be displayed randomly later
        answers = []

        # Storing correct and incorrect answers
        incorrect_answers = quizDump['results'][i]['incorrect_answers']
        # Decoding Answers to UTF-8
        for a in incorrect_answers:
            incorrect_decoded_answer = base64.b64decode(a).decode('utf-8')
            answers.append(incorrect_decoded_answer)
        
        # Storing and Decoding correct answers
        correct_answer = quizDump['results'][i]['correct_answer']
        correct_decoded_answer = base64.b64decode(correct_answer).decode('utf-8')

        answers.append(correct_decoded_answer)

        # Printing answers in random order
        rand = random.sample(answers, len(answers))

        # List for Answer Numbers
        answer_numbers = [1,2,3,4]
        # Key Value Pairs Pairing answer numbers with answers!
        answers_dictionary = {answer_numbers[i]:rand[i] for i in range(len(answer_numbers))}

        #print(answers_dictionary)
        for key,value in answers_dictionary.items():
            print('{}. {}'.format(key,value))
            
        # Getting the users answer
        answer = input('Please enter your answer: ')
        answers_to_integer = int(answer)
    
        while answers_to_integer not in range(0,5):
            answers_to_integer = input('Please enter your answer: ')
            answers_to_integer = int(answer)

        print('The correct answer was: ' + correct_decoded_answer)
        
        #print(answers_dictionary.keys())

        # Adding up the score if the answer is correct
        answer_check = answers_dictionary[answers_to_integer]
        print('Your answer was '+ answer_check)

        if answer_check == correct_decoded_answer:
            score = score + 1

    # Points Summary
    print('==========================================================================')
    print('Thank you for playing.') 
    print('===============POINTS TOTAL===============')
    print('Your total score is ' + str(score))

    # Asking the user if they would like to play again. 
    play_again = input('Would you like to play again? (Please enter y/n): ')
    if play_again == 'y':
        main()
    else:
        return   

if __name__ == '__main__':
    main()



