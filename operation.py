from datetime import datetime
from read import *
from write import *


def rent_equipment():
    dictionary = notepad()
    equipment = []

    while True:
        show_equipment()
        check_rent = checking_equipment_rent()
        while check_rent <= 0 or check_rent > len(dictionary):  #
            print("Equipment does not exist.")
            print("\n")
            check_rent = int(input("Enter the ID of the equipment : "))

        print("---------------------------------------------------------------------------------------------------")
        equipment_rent_quantity = int(input("Enter the number of the equipment being rented : "))
        print("---------------------------------------------------------------------------------------------------")

        selected_equipment_amount = dictionary[check_rent][3]
        while equipment_rent_quantity <= 0 or equipment_rent_quantity > int(selected_equipment_amount):
            print("Not enough stock.")
            print("---------------------------------------------------------------------------------------------------")

            try:
                equipment_rent_quantity = int(input("Not Enough stock. Enter a valid amount : "))
            except ValueError:
                print("Error. Enter a valid number.")
                # continue
            print("---------------------------------------------------------------------------------------------------")

        dictionary[check_rent][3] = int(dictionary[check_rent][3]) - int(equipment_rent_quantity)
        file = open("rent.txt", "w")

        for values in dictionary.values():
            file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]))
            file.write("\n")
        file.close()

        equipment_name = dictionary[check_rent][0]
        equipment_quantity = equipment_rent_quantity
        equipment_price = dictionary[check_rent][2].replace("$", '')
        total_amount = int(equipment_price) * int(equipment_quantity)
        equipment.append([equipment_name, equipment_quantity, total_amount])
        rent_again = input("Do you want to rent more equipment?").upper()

        if rent_again.upper() == "NO":
            break
        elif rent_again.upper() != "YES":
            continue

    total = 0

    for q in equipment:
        total += int(q[2])
    total_cost = total
    name = bill()
    date = datetime.now()
    print("---------------------------------------------------------------------------------------------------")
    print("Rental Shop")
    print("Costumer name :" + str(name))
    print("Date : " + str(date))
    print("---------------------------------------------------------------------------------------------------")

    for q in equipment:
        print("Equipment name : ", q[0])
        print("Amount of Equipment : ", q[1])
        print("Cost of one unit : ", q[2])
        print("---------------------------------------------------------------------------------------------------")
    print("Total cost : $" + str(total_cost))
    print("---------------------------------------------------------------------------------------------------")

    rent_bill(name, date, equipment, total_cost)


def return_equipment():
    dictionary = notepad()
    equipment_return = []
    fine_amount = 0
    fine_overdue = 0
    return_again = True
    while return_again:
        show_equipment()
        check_return = checking_equipment_return()

        # Valid ID
        while check_return <= 0 or check_return > len(dictionary):  #
            print("Please enter a proper equipment number : ")
            print("\n")
            check_return = int(input("Please enter the equipment ID you want to return: "))

        equipment_return_quantity = int(input("Please enter the amount equipment you want to return: "))

        # Valid quantity

        selected_equipment_amount = dictionary[check_return][3]
        while equipment_return_quantity < 0 or equipment_return_quantity > int(selected_equipment_amount):
            print("Enter valid number of days.")
            print("\n")
            try:
                equipment_return_quantity = int(input("Enter a valid amount of days : "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            print("---------------------------------------------------------------------------------------------------")

        # Update the text file
        dictionary[check_return][3] = int(dictionary[check_return][3]) + int(equipment_return_quantity)
        file = open("rent.txt", "w")

        for values in dictionary.values():
            file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]))
            file.write("\n")
        file.close()
        # getting user purchased equipments

        equipment_name = dictionary[check_return][0]
        equipment_quantity = equipment_return_quantity
        equipment_price = dictionary[check_return][2].replace("$", '')
        total_amount = int(equipment_price) * int(equipment_quantity)
        try:
            days_rented_for = int(input("Enter the number of days rented: "))
            if days_rented_for < 1:
                print("Please enter proper amount of days.")  # print statement
            else:
                if days_rented_for <= 5:
                    fine_amount = 0
                elif days_rented_for % 5 != 0:
                    fine_overdue = (int(days_rented_for // 5) + 1)
                    fine_amount = int((fine_overdue / 5)) * int(equipment_price)
                else:
                    fine_amount = (days_rented_for - 5) * int(equipment_price)

                yes_or_no = input("Do you want to return more equipment?").upper()

                if yes_or_no == "YES":
                    print("\n")
                    return_again = True
                else:
                    return_again = False
                total_amount = 0
                if yes_or_no == "YES":
                    return_again = True
                else:
                    total = 0
                    for q in equipment_return:
                        total = total + int(q[3])
                    total_amount = total + fine_amount
                
        except ValueError:
            print("Error. Please enter proper amount of days.")
            print("\n")

        equipment_return.append(
            [equipment_name, equipment_quantity, total_amount, days_rented_for, fine_amount])
        # Ask the user if they want to continue selecting 
        print("---------------------------------------------------------------------------------------------------")
        print("\n")

    total = 0
    for q in equipment_return:
        total += int(q[3])
    total_amount = total
    date = datetime.now()
    name = bill()
    print("Rental shop")
    print("Costumer name:" + str(name))
    print("Date : " + str(date))
    print("Name of returned equipment : ")

    for q in equipment_return:
        print(q[0], "\t\t", q[1], "\t\t", q[2], "\t\t", "$", q[3])
    print("\n")
    print("Fine: $" + str(fine_amount))
    print("Total cost : $" + str(total_amount))
    return_bill(name, date, equipment_return, total_amount)
