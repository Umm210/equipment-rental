def show_equipment():
    print("S.N.", "     |Name", "\t\t\t\t\t", "|Brand", "\t", "       |Price", "\t", "      |Quantity")
    print("-----------------------------------------------------------------------------------------------")
    s = 1
    notepad = open("rent.txt", "r")

    for line in notepad:
        print(s, "\t" + line.replace(",", "\t"))
        s += 1
    print("-----------------------------------------------------------------------------------------------")

    notepad.close()


def rent_bill(name, date, rented_equipment, total_amount):
    print("---------------------------------------------------------------------------------------------------")
    with open(name + ".txt", "w") as text:
        text.write("---------------------------------------------------------------------------------------------------")
        text.write("Rental Shop Bill")
        text.write("\n")
        text.write("Costumer name : " + str(name) + "\n")
        text.write("Date and time of purchase: " + str(date) + "\n")
        text.write("\n")
        text.write("Equipment Quantity Total")
        text.write("\n")
        for q in rented_equipment:
            text.write(str(q[0]) + "\t" + str(q[1])  + "\t" + "$" + str(q[2]) + "\n")

        text.write("Total amount : $" + str(total_amount))


def return_bill(name, date, user_returned_equipments, total_amount):
    print("---------------------------------------------------------------------------------------------------")
    with open(name + ".txt", "w") as text:
        text.write("\n")
        text.write("Rental Shop")
        text.write("\n")
        text.write("Costumer name : " + str(name) + "\n")
        text.write("Date and time of purchase: " + str(date) + "\n")
        text.write("\n")
        text.write("Equipment Quantity Total")
        text.write("\n")
        for q in user_returned_equipments:
            text.write(str(q[0]) + "\t\t" + str(q[1]) + "\t\t" + "$" + str(q[2]) + "\n")

        text.write("Total amount : $" + str(total_amount))


def bill():
    name = input("Enter your name : ")

    return name
