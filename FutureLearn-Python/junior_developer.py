class Validator:
    ''' A class for validating user  data.
        Takes 5 argument.
        Methods:
            < name_checker() >
            < email_check() >
            < phone_checker() >
            < domain_checker() >
            < notes_checker() >
        Parameters:
            name, email, phone, domain, notes
            
    '''

    # Initialize attributes of the validator class

    def __init__(self, name, email, phone, domain, notes):
        self.name = name
        self.email = email
        self.phone = phone
        self.domain = domain
        self.notes = notes

    def email_checker(self):
        """     
            Method takes < USER EMAIL >.
            Then perform basic checks on  < USER EMAIL >..
            Returns a validated   < USER EMAIL >..
        """
        # counter flag .
        counter = 0

        email_length = len(self.email)

        dot_char = self.email.find('.')

        at_char = self.email.find('@')

        # It must contain at least one alphabet.
        # Email cannot start with @
        # @ and dot cannot exist together.
        # There must be at least one character before @ and after the dot.

        # Check for all conditions.

        # Using for loop to confirm If email contains at least one alphabet.
        
        if self.email:


            for i in range(0, at_char):
                if (self.email[i] >= 'a' and self.email[i] <= 'z' or self.email[i] >= 'A' and self.email[i] <= 'Z'):
                    counter += 1


                    if (counter > 0 and at_char > 0 and (dot_char - at_char) > 0 and (dot_char + 1) < email_length):
                        return self.email
                    else:
                        return
                else:
                    return None

        else:
            return None
            
    def phone_check(self):
        """     
            Method takes < USER PHONE >.
            Then perform basic checks on  < USER PHONE >..
            Returns a validated   < USER PHONE >..
        """

        # Check If user input is not blank.

        if self.phone:

            # If length  is equal to eleven.
            cell_length = len(self.phone)    
            if cell_length == 11:

                # Confirm user input is infact an integer.

                try:

                    cell_length = int(cell_length)
                    return self.phone
                
                
                # Except User phone is not integer catch error and return None
                except ValueError:
                    return
            
            # Else return None if user phone length is not equal to length of the UK numbers.
            else:

                return 
        
        # Else return None if user entered a blank.
        else:

            return

    def name_checker(self):
        """
            class method prompts user for <name input > and returns a validated < name >
     
        """
        # Check If user input is not blank.
        
        if self.name:

            # Check If user input is made up of alphabets.

            if self.name.isalpha():

                # Return neatly formatted name in title case.
                
                return self.name.title()

                # Else return None
            else:
                return

        # Else return None

        else:
            return

    def domain_checker(self):
        """      
            <A method to check domain.>
     
            """
        if self.domain:
            return self.domain
        else:
            return

    def notes_checker(self):
        """      
            <A method to check notes.>
     
            """
        if self.notes:

            return self.notes

        else:
            return

# Import statement

import json



# To Do: Make data persistence .

# Beginning of while loop.

# rolling flag

rolling = 0

while not rolling:
    
    # An empty Dictionary to store user information.

    user_info = {}

    # Active flag
    active = 0
    while not active:

        # Offer user an option.

        user_option = input('Please type:\n("Y") to save user information\n("Q") to Quit.')
        

        # Check for blank user input.

        if user_option:

            if user_option.lower() == 'y':
                name = input('Enter Name: ')
                email = input('Enter Email: ')
                phone = input('Enter Phone: ')
                domain = input('Enter Domain: ')
                notes = input('Enter Notes: ')

                # Make an Instance of the Validator class.

                # Then check all entries.


                input_validator = Validator(name, email, phone, domain, notes)
                name = input_validator.name_checker()
                email = input_validator.email_checker()
                phone = input_validator.phone_check()
                domain = input_validator.domain_checker()
                notes = input_validator.notes_checker()

                

                user_info['name'] = name
                user_info['email'] = email
                user_info['phone'] = phone
                user_info['domain'] = domain
                user_info['notes'] = notes

                
                
                
                # Ask user if they would like to edit or delete.
                

                edit_or_delete = input('Please type("E") to Edit.\n("D") to Delete.\n("Q") to Quit.')

                if edit_or_delete.lower() == 'e':

                    


                    print('Enter "name" to change name')
                    print('Enter "email" to change email')
                    print('Enter "phone" to change phone number')
                    print('Enter "domain" to change domain')
                    print('Enter "notes" to change notes')

                    what_to_edit = input('What would you like to change?\n')
                    if what_to_edit.lower() == 'phone':

                        value_change = input('phone value: ')
                        
                        user_info[phone] = value_change

                    elif what_to_edit.lower() == 'name':
                        value_change  = input('name value: ')
                        
                        user_info[name] = value_change 

                    elif what_to_edit.lower() == 'email':

                        value_change = input('email value: ')

                        user_info[email] = value_change

                    elif what_to_edit.lower() == 'domain':

                        value_change = input('domain value: ')

                        user_info[domain] = value_change


                    elif wwhat_to_edit.lower() == 'notes':

                        value_change = input('notes value: ')

                        user_info[notes] = value_change

                
                elif edit_or_delete.lower() == 'd':
                    
                    double_check = input('Enter ("Y") to confirm delete.\n Enter("N") to abort delete operation.')
                    # If user confirms delete action.
                    # Then clear user info from dictionary.
                    if double_check.lower() == 'y':
                        print('Deleting and updating. . . .')
                        user_info.clear()

                    else:

                        active = 1

                # Else Break.
                elif edit_or_delete.lower() == 'q':

                    active = 1

            else:

                active = 1
        else:
            active = 0



    print('User Information --:\n')

    # Making data persistent.

    filename =  'user_info.json'
    with open(filename, 'w') as file_obj:
        json.dump(user_info, file_obj)


    filename = 'user_info.json'
    with open(filename) as file_obj:
        user_info = json.load(file_obj)
        for data, value in user_info.items():
            print(f"{data}: {value}")
        

        
    # Save another user.
    save_more_user = input('Add more users?\nType (Y/N): ')
    if save_more_user.lower() == 'y':

        rolling = 0
    elif save_more_user.lower() == 'n':

        rolling = 1
