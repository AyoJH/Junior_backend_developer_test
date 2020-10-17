 
# Please note that you will need to apply knowledge from prior weeks in order to complete this assignment!
# For this assignment, you need to modify the program you created in the While Loops Assignment $ 
# Re-organize your submission to eliminate redundant code. 
# Promote code re-use, and use functions to gather each piece of data.
 
 
# ------------------------------ Creating functions to carry out the task required by the program. ------------------------------ #
def employee_id():
    """Function takes no arguments.
 
        Function prompts for < Employee ID > from user and returns < Employee ID >
 
        """
    # Flag to keep while loop under control.
    num_ok = False
 
 
    while not num_ok:
        num = input('Enter number:')
 
 
        # Check for bad characters in user input and terminate if  bad character is found.
        # If user input is not blank.
        if num:
            
 
            # Checking the user input to see if it is truly integer.
            # Using try and  except statement to control error output.
            try:
 
                int(num)
                num_ok = True
                
                # If length  is less than or equal to seven.
                if len(num) <= 7:
                    return num
 
                else:
                    num_ok = False
                    
            # If any error in user input ask for user input again.
            except:
                num_ok = False
                
        # Else ask for user input again.       
        else:
            num_ok = False
 
def employee_name():
    """ Function takes no arguments.
 
        Function prompts user for <name input > and return < name >
 
        """
 
    # A flag to control the while loop.  
    name_ok = False
    
    # Characters that must not be included in user input.
    # characters =  list('!"@#$%^&*()_=+,<\>/?;:[]{}\).')
    characters =  list('! " @ # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \ )')
 
    while not name_ok:
 
 
        # Ask user for name.
        name = input('Enter name:')
        for char in characters:
            if char not in name:
                return name.title()
                    

            else:
                name_ok = False

 
 
def employee_address():
    """ Function takes no arguments.
 
        Function prompts for employee < ~address~ > as input from user and returns < ~address~ >
 
        Function returns a None type if no input was given by user.
 
    """
        
    bad_chars = list("!\"'@$%^&*_=+<>?;:[]{}).")
 
    # Flag keeps while loop under control. 
    address_ok = False   
 
 
    while not address_ok:
 
        # Get user input.
        address = input('Enter postal address: ')
 
        # Check to make sure user input is not blank.
        if address:
 
            #Empty string to help wih the check along the way.
            new_address = ''
 
            # For loop to iterate through elements of user input
            for element in address:
                
                # Validating address by check for numeric, alphabet and space(' ') character.
                if ((element.isnumeric() or element.isalpha()) or element.isspace()):
 
                    # If condition above is true concatenate the letter with  empty string from above.
                    new_address += element
 
                    # If element of address in the list of bad characters ask user for input.
                    if element in bad_chars:
                        address_ok = False
 
                    # Else return user input.
                    else:
                        return address
                        
        # Else inform user they did not provide an address.              
        else:
            return 'You did not provide an address.'
 
 
def employee_email():
    """Function takes no arguments.
 
        Function prompts for employee < email > as input from user and returns < email >.
        
        """
    # Active flag for while loop.
    active = False
 
    # Characters that mjust not be included in user input.
    characters =  list('!"\'#$%^&*()=+,<>/?;:[]{}\)')
 
 
    while not active:
        email = input('Enter email:')
 
        
        # Check for bad characters in user input and terminate if  bad character is found.
        # Blank check
        if email:
 
            #Empty string to help wih the check along the way.
            new_email = ''
 
            # For loop to iterate through elements of user input.
            for letter in email:
 
 
                # Check for numbers, alphabets, '@' symbol and '.'.
                if (letter.isnumeric() or letter.isalpha()) or (letter == '@' or letter == '.'):
 
                     # If condition above is true concatenate the letter with our empty string from above.
                    new_email += letter
 
 
                    #  if any bad character present in user input.
                    if letter in characters:
 
                        # Get the right input from user
                        active = False
                        
                    else:
                        return email
 
                # If user input does not have characters of a real email address.
                # Ask user to enter input.
                else:
                    
                    active = False
                  
                if not active:
                    
                    email = input('Email was not entered properly\nPlease try again:')
 
 
 
                
# <<<---------------------------------------- Start of the program ---------------------------------------->>> #
 
# Create Empty list to append dictionary items at the end of the program.
employee_data = []
 
# While loop flag.
count = 0
 
 
# Inform user of maximum data storage per session.
print('You can store upto 5 employee datas per session.')
 
# Ask user for input.
users = input('Number of employee datas to store ?: ')

# Validate users is not a blank input.
if users:
    
    # Error Handling.
    try:
        users = int(users)

        # Another check to keep users under limit of 5.
        if users > 5:
            print('Please be sure to enter an integer not greater than 5.')

        # Users less than 5 .
        # Run the while loop for the value of users.    
        else:

            # While loop runs till counter flag is equal to users.
            while count < users:
 
 
                # Appending dictionary object to list.
                # Calling functions inside the list append aoperation. 
                employee_data.append({'ID num': employee_id(),  'Name': employee_name(), 'Employee Address': employee_address(), 'Employee Email': employee_email() })
                count = count + 1



    except:
        print('Please be sure to enter an integer.')

else:
    print('Please be sure you have not entered a blank.')

print(employee_data)
