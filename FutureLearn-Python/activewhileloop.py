##Week 8 - While Loops Assignment
##
##
##Please note that you will need to apply knowledge from prior weeks in order to complete this assignment!
##
##
##For this assignment, you need to modify the program you created in the User Input Assignment so that it can take up to 5 employees  
##worth of information.
##
##Also, when a user enters improper data, the program asks the user to re-enter it before continuing on.
##
##
##As employee information is added, create a list of dictionaries that hold all of the information.
##
##
##And the end of your program, print out the list.

# Data we need to store
employee_names = ['Jackie Grainger','Jignesh Thrakkar','Dion Green','Jacob Gerber', 'Sarah Sanderson', 'Brandon Heck','David Toma', 'Charles King']

employee_salary = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]

employee_numbers = [1121, 1122, 1127, 1132, 1137, 1138, 1152, 1157]

hourly_rate = [28.886, 32.825, 37.375, 31.616000000000003, 30.485, 33.592, 29.445, 30.875]


#####

# Empty list to store the data above
list_of_dict = []


# variable that will help us retrieve values from one of the lists
index_count = 0


while index_count < 5:

    # Introduce our dictionary template, assign it the current values in our lists as we loop through them
    # Append the newly created dictionary to the list of dicts
    list_of_dict.append({'name':employee_names[index_count], 'number': employee_numbers[index_count],
                     'salary':employee_salary[index_count],
                     'hourly rate': hourly_rate[index_count]})
    # Increment index count variable.
    index_count += 1
        
# Printing list of dicts.
print(list_of_dict)
