quiz = {
    'question1': {
        'question': 'What is the capital of USA?',
        'answer': 'Washington'
    },
    'question2': {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    'question3': {
        'question': 'What is the capital of Japan?',
        'answer': 'Tokyo'
    },
    'question4': {
        'question': 'What is the capital of Austria?',
        'answer': 'Vienna'
    },
    'question5': {
        'question': 'What is the capital of Brazil?',
        'answer': 'Brasília'
    },
    'question6': {
        'question': 'What is the capital of Egypt?',
        'answer': 'Cairo'
    },
    'question7': {
        'question': 'What is the capital of Germany?',
        'answer': 'Berlin'
    },
    'question8': {
        'question': 'What is the capital of Israel?',
        'answer': 'Jerusalem'
    },
    'question9': {
        'question': 'What is the capital of Mexico?',
        'answer': 'Mexico City'
    },
    'question10': {
        'question': 'What is the capital of Spain ?',
        'answer': 'Madrid'
    }
}

score=0

for key,value in quiz.items():
    print(value['question'])
    answer=input("Answer? ")

    if answer.lower()==value['answer'].lower():
        print('Correct!')
        score+=1
        print("Your Score Is: "+str(score))
        print('')
        print('')

    else:
        print('Incorrect:( The Right answer is) \n' + value['answer'] )
        print("Your Score Is: "+str(score))
        print('')
        print('')


print("Your Final Score Is: "+str(score)+ " Out of 10 questions correctly .")
print('Your percentage is: ' +str((score/10)*100)+ " %")
