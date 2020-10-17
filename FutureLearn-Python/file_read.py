def open_file(file):
    """Prints text from a file line by line"""
    try:


        # Open the from source folder as a file object.
        with open(file, 'r') as file_obj:

           # Create line obj.
            lines = file_obj.readlines()
            
        # Loop through file object.
        for line in lines:    

            # Print each line of text in file object.
            return line

    except Exception as e:
        print(e)
##def open_file(file):
##    """Prints text from a file line by line"""
##    try:
##        with open(file, 'r') as file_obj:
##            lines = file_obj.readlines()
##        for line in lines:
##            print(line.rstrip())
##    except Exception as e:
##        print(e)
##def open_file(file):
##    """Prints text from a file line by line"""
##    try:
##        with open(file, 'r') as file_obj:
##            lines = file_obj.readlines()
##        for line in lines:
##            print(line.rstrip())
##    except Exception as e:
##        print(e)
