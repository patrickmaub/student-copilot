from summary import *
from translate import *
from brainstorm import *
from findquotes import *
from outline import *
from studyguide import *
print('Welcome to CoStar AI. Please select a capability.')
print('1. Summarizer')
print('2. Translator')
print('3. Brainstormer')
print('4. Quote Finder')
print('5. Outline')
print('6. StudyGuide')
# 1,500 words ~= 2048 tokens


def menu():
    user_choice = input()
    if user_choice == '1':
        summary()

    elif user_choice == '2':
        translate()
        menu()
    elif user_choice == '3':
        brainstorm()
        menu()
    elif user_choice == '4':
        quotes()
        menu()
    elif user_choice == '5':
        outline()
        menu()
    elif user_choice == '6':
        study_guide()
        menu()
    else:
        print('Please enter a valid choice.')


menu()
