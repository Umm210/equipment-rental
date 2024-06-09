from datetime import datetime
#from read import *
from operation import *

rental_title()#title

continue_program = True #program continues while this is true
while continue_program:

    try:
        selecting_options = menu()
        
        if selecting_options == 1:  #showing equipment
            show_equipment()

        elif selecting_options == 2:  #renting
            rent_equipment()
            print("---------------------------------------------------------------------------------------------------")
            print("Item has been rented.")
            print("---------------------------------------------------------------------------------------------------")

        elif selecting_options == 3:  #returning
            return_equipment()
            print("---------------------------------------------------------------------------------------------------")
            print("Item has been returned.")
            print("---------------------------------------------------------------------------------------------------")

        elif selecting_options == 4:  #exiting
            print("Thank you.")
            continue_program = False
        else:
            print("---------------------------------------------------------------------------------------------------")
            print("Enter a valid option.")
            print("---------------------------------------------------------------------------------------------------")

    except ValueError:  #number exception
        print("---------------------------------------------------------------------------------------------------")
        print("Error, Enter a valid option.")
        print("---------------------------------------------------------------------------------------------------")
