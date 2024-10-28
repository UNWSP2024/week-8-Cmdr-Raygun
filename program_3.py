# Author: Andrew Bittner
# Date: 10/25/2024

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

def quiz_user(answers, prompt, q_ct=5):
    score = 0
    for num in range(q_ct):
        terms = random.sample(list(answers), k = q_ct)
        key = terms[num]
        value = answers[key]
        prompt_new = prompt.replace('_TERM_', key)
        response = input(prompt_new)
        for ind in range(len(value)):
            correct = False
            if response.lower().strip() == value[ind].lower():
                correct = True
            if correct:
                break
        if correct:
            print('That\'s correct!')
            score += 1
        else:
            print('Sorry, that\'s incorrect.')
        correct = False
    print(f'You scored {score} out of {q_ct} points.')


def main():
    state_capitals = {'Alabama': ['Montgomery'], 'Alaska': ['Juneau'], 'Arizona': ['Phoenix'],
                      'Arkansas': ['Little Rock'], 'California': ['Sacramento'], 'Colorado': ['Denver'],
                      'Connecticut': ['Hartford'], 'Delaware': ['Dover'], 'Florida': ['Tallahassee'],
                      'Georgia': ['Atlanta'], 'Hawaii': ['Honolulu'], 'Idaho': ['Boise'], 'Illinois': ['Springfield'],
                      'Indiana': ['Indianapolis'], 'Iowa': ['Des Moines'], 'Kansas': ['Topeka'],
                      'Kentucky': ['Frankfort'], 'Louisiana': ['Baton Rouge'], 'Maine': ['Augusta'],
                      'Maryland': ['Annapolis'], 'Massachusetts': ['Boston'], 'Michigan': ['Lansing'],
                      'Minnesota': ['St. Paul', 'Saint Paul'], 'Mississippi': ['Jackson'],
                      'Missouri': ['Jefferson City'], 'Montana': ['Helena'], 'Nebraska': ['Lincoln'],
                      'Nevada': ['Carson City'], 'New Hampshire': ['Concord'], 'New Jersey': ['Trenton'],
                      'New Mexico': ['Santa Fe'], 'New York': ['Albany'], 'North Carolina': ['Raleigh'],
                      'North Dakota': ['Bismarck'], 'Ohio': ['Columbus'], 'Oklahoma': ['Oklahoma City'],
                      'Oregon': ['Salem'], 'Pennsylvania': ['Harrisburg'], 'Rhode Island': ['Providence'],
                      'South Carolina': ['Columbia'], 'South Dakota': ['Pierre'], 'Tennessee': ['Nashville'],
                      'Utah': ['Salt Lake City, Salt Lake'], 'Vermont': ['Montpelier'], 'Virginia': ['Richmond'],
                      'Washington': ['Olympia'], 'West Virginia': ['Charleston'], 'Wisconsin': ['Madison'],
                      'Wyoming': ['Cheyenne']}
    quiz_user(state_capitals, 'What is the capital of _TERM_? ')
    exit_sequence()


if __name__ == '__main__':
    main()