# Active flag to control while loop.
active = 0

# Highscore variable to keep track of high scores.
highscore = 0
while not active:
    # Score and answers variable to keep track scores and answer during Quiz.
    score = 0
    correct_answer, user_answer = 0, 0

    # Three print statements.
    # Welcome message.
    # How-to-answer/win Quiz.
    print("Welcome to the Maths Quiz")
    print("Answer all questions to score maximum points: ")
    print("Please enter between 0-3 for Quiz of your choice: ")
    
    questions = [
        'Question 0: What is the product of 2x2x2 ?',
        'Question 1: What is the product of 2x2x2x2 ?',
        'Question 2: What is the product of 2x2x2x2x2 ?',
        'Question 3: What is the product of 2x2x2x2x2x2 ?',
    ]
    
    answers = [8, 16, 32, 64]

    # Take choice of question as input from player.
    question_choice = input('Your choice of -->> ')

    if question_choice:

        try:
            question_choice = int(question_choice)
            question = questions.pop(question_choice)
            print(question)
        except(IndexError)(ValueError):
            print('The quiz choice is out of range and make sure an integer is entered.')
            continue

    else:
        print('Choose btw integer 0-3.')
        continue

    # Take user answer as input.
    # Check user answer isn't blank.
    # Check that user answer is an integer.
    # Assign the correct answer to the correct_answer variable.
    # using pop method on answers list and question choice as the index to pop.
    # Update game score if user answer is the correct answer
    # Print correct answer, user answer and score.

    user_answer = input('Your answer --> ')
    correct_answer = answers.pop(question_choice)
    if user_answer:

        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                score += 1
                print('Correct Answer-->', correct_answer)
                print('User Answer -->', user_answer)
                print('Your score is', score)

            # Else print the incorrect answer from user.
            # Print the correct answer.
            # Print game score.

            else:
                print('Incorrect Answer:', user_answer)
                print('The Correct Answer is ', correct_answer)
                print('You scored ', score)
        except ValueError:
            print('Please make sure an integer is entered.')
            continue

    else:
        continue

    # Check using if-else statement to confirm players answer is correct. 
    if score > highscore:
        highscore = score
        print('The current highest score is', highscore)

        # Else if score is not greater than highscore.
        # Print highest score and player score.
    else:
        print('The current highest score is ' + str(highscore) +'\nYour score -->',score)

    # Give user option of playing again.
    # Use if-else statement to check user option.

    print('Type (Y) for more Quiz and (Q) for Quit ? ')
    option = input('Your Option-->> ')
    highscore = score
    print('The current highest score is ',highscore)
    
    if option.lower() == 'y':
        print('Starting a new game...')
        continue
    else:
        print('Thanks for playing, check back soon!')
        break
