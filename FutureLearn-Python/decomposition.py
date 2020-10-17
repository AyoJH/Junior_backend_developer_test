# To explain how the code will work I will again use ‘decomposition’.

# The program needs to be extended to read the high score from a file and 
# write it back if the player beats it.

# Load the high score from highscore.txt
# Set the current score to zero
# Ask the questions and adjust the current score as before
active = False
while not active:
    import os

    with open('highscoretry.txt', 'r') as f:
        score = 0
        highscoretry = f.read()
        try:
            # highscoretry = f.read()
            highscoretry = int(highscoretry)
            print("The highest score previously was:\n", highscoretry)
            print("Welcome to the Maths Quiz")
            print("Answer all questions to score maximum points: ")
            print("Please enter between 0-3 for Quiz of your choice: ")
        except(ValueError):
            # Return to beginnign of the game if try unsuccessful
            continue

        questions = [
            'Question 0: What is the product of 2x2x2 ?',
            'Question 1: What is the product of 2x2x2x2 ?',
            'Question 2: What is the product of 2x2x2x2x2 ?',
            'Question 3: What is the product of 2x2x2x2x2x2 ?'
            ]

        answers = [8, 16, 32, 64]
        print('## Starting Game. . . .')
        print('To choose quiz enter an integer.')
        # Take choice of question as input from player.
        question_choice = input('Your choice of -->> ')

        if question_choice:

            try:
                question = questions.pop(int(question_choice))                            
                print(question)
                user_answer = int(input('Your answer --> '))
                correct_answer = answers.pop(int(question_choice))
                
            except (IndexError)(ValueError):
                
                # Return to the beginning of game if tru unsuccessful.
                continue

            if user_answer and user_answer == correct_answer:
                user_answer = correct_answer
                score += 1
                print('Your answer is correct', user_answer)
                print('You scored: ', score)

            else:
                score = 0
                print('Incorrect answer:', user_answer)
                print('You scored: ', score)


            # If score is greater than highscoretry.
            # Make score data persistent by writting it to file. 
            if score >= highscoretry:
                highscoretry = score

                with open('highscoretry.txt', 'w') as f:
                    f.write(str(highscoretry))

            else:
                print('You have not set a new high score better luck next time!')
                
            option = input('Type (Y) to continue and (Q) to Quit ? ')
            if option.lower() == 'y':
                print('Starting a new game...')
                continue
            
            else:
                 print('Thanks for playing, check back soon!')
                 break
        
        # Else if user supplied blank choice.
        else:

            # Return to beginning of game.
            continue

