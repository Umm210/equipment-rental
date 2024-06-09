def rental_title():
    print("---------------------------------------------------------------------------------------------------")
    print("Rental Shop")


def menu():
    print("---------------------------------------------------------------------------------------------------")
    print("1. Show equipment available for renting")
    print("2. Rent an equipment")
    print("3. Return an equipment")
    print("4. EXIT")
    print("---------------------------------------------------------------------------------------------------")
    selecting_options = int(input("Select an option: "))

    return selecting_options


def notepad():
    with open("rent.txt", 'r') as text_file:
        dictionary = {}
        equipment_number = 1

        for line in text_file:
            line = line.replace("\n", "")
            dictionary[equipment_number] = line.split(",")

            equipment_number = equipment_number + 1

        text_file.close()

        return dictionary


def checking_equipment_rent():
    check_rent = int(input("Enter the equipment number for renting : "))
    return check_rent


def checking_equipment_return():
    check_return = int(input("Enter the equipment number to return : "))
    return check_return



