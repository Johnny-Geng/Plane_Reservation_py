# Johnny Geng, johnnyge@usc.edu

# Description:
# This program is an automated reservations system designed to assign and check plane seats.

def main():
    # Set-up:
    firstFilledSeats = 0
    firstMaxSeats = 4
    econFilledSeats = 0
    econMaxSeats = 6
    numFilledSeats = 0
    TOTAL_SEATS = 10
    firstSeatList = ["Empty", "Empty", "Empty", "Empty"]
    econSeatList = ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty"]
    menu = "default"

    # Menu:
    while menu != "-1":

        menu = input("\n1: Assign Seat\n2: Print Seat Map\n3: Print Boarding Pass\n-1: Quit\n\n> ")
        # Option 1: Assign Seat
        if menu == "1":
            if numFilledSeats < TOTAL_SEATS:
                name = input("Please enter your first name: ")
                name = name.capitalize()
                # Check Class (First / Economy):
                Class = input("Type 1 for First Class or Type 2 for Economy.\n> ")
                # Choose First Class:
                if Class == "1":
                    if firstFilledSeats < firstMaxSeats:
                        number = firstSeatList.index("Empty")
                        firstSeatList[number] = name
                        firstFilledSeats += 1
                        numFilledSeats += 1
                    # Surpass First Class Capacity:
                    else:
                        print("The First Class section is full. Would you like to be placed in "
                              "the Economy Class section?")
                        question = input("Type: (y/n)\n>")
                        if question.lower() == "y":
                            number = econSeatList.index("Empty")
                            econSeatList[number] = name
                            econFilledSeats += 1
                            numFilledSeats += 1
                        elif question.lower() == "n":
                            print("Next flight leaves in 3 hours.")
                        # Error Check (y/n)
                        else:
                            print("Invalid choice. No seat will be assigned. Please try again.")
                # Choose Economy Class:
                elif Class == "2":
                    if econFilledSeats < econMaxSeats:
                        number = econSeatList.index("Empty")
                        econSeatList[number] = name
                        econFilledSeats += 1
                        numFilledSeats += 1
                    # Surpass Economy Class Capacity:
                    else:
                        print("The Economy Class section is full. Would you like to be placed in "
                              "the First Class section?")
                        question = input("Type: (y/n)\n>")
                        if question.lower() == "y":
                            number = firstSeatList.index("Empty")
                            firstSeatList[number] = name
                            firstFilledSeats += 1
                            numFilledSeats += 1
                        elif question.lower() == "n":
                            print("Next flight leaves in 3 hours.")
                        # Error Check (y/n)
                        else:
                            print("Invalid choice. No seat will be assigned. Please try again.")
                # Error Check: (1/2)
                else:
                    print("Invalid choice. No seat will be assigned. Please try again.")
            else:
                print("Next flight leaves in 3 hours.")

        # Option 2: Print Seat Map
        elif menu == "2":
            print("***************************************")
            print("     ---First Class---")
            seatNumber = 0
            # First Class Seat Map:
            for seatName in firstSeatList:
                print("     Seat #" + str(seatNumber + 1) + ":  " + seatName)
                seatNumber += 1
            print("     ---Economy Class---")
            # Economy Class Seat Map:
            for seatName2 in econSeatList:
                print("     Seat #" + str(seatNumber + 1) + ":  " + seatName2)
                seatNumber += 1
            print("***************************************")

        # Option 3: Print Boarding Pass
        elif menu == "3":
            print("Type 1 to get Boarding Pass by seat number")
            print("Type 2 to get Boarding Pass by name")
            questionBP = input(">")
            # By Seat Number:
            if questionBP == "1":
                questionNumber = input("What is the seat number: ")
                if questionNumber.isdigit():
                    numSeat = int(questionNumber)
                    if numSeat in range(1, 11):
                        # For First Class Passenger:
                        if numSeat in range(1, 5):
                            print("======= BOARDING PASS =======")
                            print("     Seat #: " + questionNumber)
                            print("     Passenger Name: " + firstSeatList[numSeat - 1])
                            print("=============================")
                        # For Economy Class Passenger:
                        else:
                            print("======= BOARDING PASS =======")
                            print("     Seat #: " + questionNumber)
                            print("     Passenger Name: " + econSeatList[numSeat - 5])
                            print("=============================")
                    else:
                        print("Invalid number--no boarding pass found")
                else:
                    print("Invalid answer. Please try again.")
            # By Name:
            elif questionBP == "2":
                questionName = input("Enter passenger name: ")
                questionName = questionName.capitalize()
                # For First Class Passenger:
                if questionName in firstSeatList:
                    numPassengerSeat = firstSeatList.index(questionName) + 1
                    print("======= BOARDING PASS =======")
                    print("     Seat #: " + str(numPassengerSeat))
                    print("     Passenger Name: " + questionName)
                    print("=============================")
                # For Economy Class Passenger:
                elif questionName in econSeatList:
                    numPassengerSeat = econSeatList.index(questionName) + 5
                    print("======= BOARDING PASS =======")
                    print("     Seat #: " + str(numPassengerSeat))
                    print("     Passenger Name: " + questionName)
                    print("=============================")
                else:
                    print("No passenger with name " + questionName + " was found")
            else:
                print("Invalid choice. Please try again.")

        # Quit
        elif menu == "-1":
            menu = "-1"

        # Other numbers
        else:
            print("Invalid choice. Please try again.")
    print("Have a nice day!")

main()