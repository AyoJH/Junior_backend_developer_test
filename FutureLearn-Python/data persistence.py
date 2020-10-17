import clearbit
import json



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

import clearbit

## OAuth
clearbit.key = 'sk_da14e16c2943eee59eddf40a42983144'

class Clearbitscrapper:

    def __init__(self, diction, string):
        self.diction = diction
        self.string =string

    

    def search_by_email(self):
        '''
           Method returns a person response object.

        '''
        import json

        # Get
        
        # person_response = clearbit.Enrichment.find(email=self.string, stream = True)

        company_person = clearbit.Enrichment.find(email=self.string)

        if 'pending' in company_person:

            # Try queued - try again later
            print('Pending response, try again!')

            

        elif 'company' in company_person:

            self.diction.update({'industry': company_person['company']['category']['industry']})
            self.diction.update({'category': company_person['company']['category']})
            self.diction.update({'description': company_person['company']['description']})
            self.diction.update({'tags': company_person['company']['tags']})
            self.diction.update({'logo': company_person['company']['logo']})

        elif 'person' in company_person:

            self.diction.update({'bio': company_person['person']['bio']})
            self.diction.update({'avatar': company_person['person']['avatar']})
            self.diction.update({'employment': company_person['person']['employment']})
            self.diction.update({'title': company_person['person']['employment']['title']})

            

        return self.diction


# Beginning of while loop.

# rolling flag

records = {}
active = 0
while True:        
    
    user_option = input('Welcome Type("Y") to save user info\n("Q") to Quit.')
    if user_option.lower() == 'y':
        name = input('Enter Name: ')
        email = input('Enter Email: ')
        phone = input('Enter Phone: ')
        domain = input('Enter Domain: ')
        notes = input('Enter Notes: ')
        
        # Make an Instance of the Validator class.
        # Validate user input calling appropriate methods.
        
        input_validator = Validator(name, email, phone, domain, notes)
        valid_name = input_validator.name_checker()
        valid_email = input_validator.email_checker()
        valid_phone = input_validator.phone_check()
        valid_domain = input_validator.domain_checker()
        valid_notes = input_validator.notes_checker()

        # Save data in dictionary.
        
        records['name'] = valid_name
        records['email'] = valid_email
        records['phone'] = valid_phone
        records['domain'] = valid_domain
        records['notes'] = valid_notes


        # Give user an option to edit.

        edit_or_delete = input('Please type("E") to Edit.\n("D") to Delete.')

        if edit_or_delete.lower() == 'e':

            print('Enter "name" to change name')
            print('Enter "email" to change email')
            print('Enter "phone" to change phone number')
            print('Enter "domain" to change domain')
            print('Enter "notes" to change notes')

            # Get the input for what user want to edit.

            what_to_edit = input('What would you like to change?\n')

            # Check

            if what_to_edit.lower() == 'phone':

                value_change = input('phone value: ')
                
                records['phone'] = value_change

            elif what_to_edit.lower() == 'name':
                value_change  = input('name value: ')
                
                records['name'] = value_change 

            elif what_to_edit.lower() == 'email':

                value_change = input('email value: ')

                records['email'] = value_change

            elif what_to_edit.lower() == 'domain':

                value_change = input('domain value: ')

                records['domain'] = value_change


            elif what_to_edit.lower() == 'notes':

                value_change = input('notes value: ')

                records['notes'] = value_change 

            # Create an instance of clearbit scrapper.

            # Supply the instance with dictionary. and email as string.
            
            bits_scrapper = Clearbitscrapper(records, records['email'])


            
            harvest = bits_scrapper.search_by_email()

            filename =  'records.json'
            with open(filename, 'w') as file_obj:
                json.dump(harvest, file_obj)

        

        elif edit_or_delete.lower() == 'd':
            double_check = input('Enter ("Y") to confirm delete.\n Enter("N") to abort delete operation.')

            # If user confirms delete action.
            # Then clear user info from dictionary.
                
            if double_check.lower() == 'y':
                        
                print('Deleting and updating. . . .')
                
                records.clear()

            else:

                active = 1


    elif user_option.lower() == 'q':

        break         

print(records)