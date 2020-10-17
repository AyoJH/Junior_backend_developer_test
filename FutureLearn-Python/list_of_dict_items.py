##Week 8 - Dictionaries Assignment
##
##Please note that you will need to apply
##knowledge from prior weeks in order to complete this assignment!This
##week, I would like you to modify the program you wrote last week so that
##it takes the data from the final employee numbers, employee names,
##employee salary, total hourly rate, and company raises lists and
##combines it into a list of dictionary items that looks like a
##database-like structure. At the end of your program, print out the final
##list.Be sure to put comments in your code that clearly mark how you are
##performing your program logic. Also, be sure to apply the lessons about
##structuring dictionaries that were covered in the lecture.  In the
##submission comments of this assignment, please place the repository URL
##of your file submission.



# Data to store
employee_names = ['Jackie Grainger','Jignesh Thrakkar','Dion Green','Jacob Gerber', 'Sarah Sanderson', 'Brandon Heck','David Toma', 'Charles King']
employee_salary = [22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75]

employee_numbers = [1121, 1122, 1127, 1132, 1137, 1138, 1152, 1157]

hourly_rate = [28.886, 32.825, 37.375, 31.616000000000003, 30.485, 33.592, 29.445, 30.875]




# Creation of empty list to store data.
list_of_dict = []


# variable that will help us retrieve values from one of the lists
index_count = 0

# Iterating over employee names
for name in employee_names:
    
    # Introduce our empty list, assign it the current values data to store as we loop through them and

    # Combines it into a list of dictionary items
    list_of_dict.append({'name':name, 'number': employee_numbers[index_count],
                         'salary':employee_salary[index_count],
                         'hourly rate': hourly_rate[index_count]})

    # Increment our current index variable.
    index_count += 1


print(f"Printing the new list of dictionary:\n\n{list_of_dict}\n\n")

print(type(list_of_dict))


