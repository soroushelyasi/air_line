import sys
from passenger import Passenger
from city import City
from flight import Flight
from airplane import Airplane

if __name__ == '__main__':
    # Make a game instance, and run the game.
    print("Welcome to airline!!!")
    while True:
        print("#1: add passenger")
        print("#2: show passengers")
        print("#3: add airplane")
        print("#4: show airplanes")
        print("#5: add city")
        print("#6: show cities")
        print("#7: add flight")
        print("#8: show flights")
        selected_action = int(input("select an action number: "))
        match selected_action:
            case 1:
                print("#1: add passenger")
            case 2:
                print("#2: show passengers")
            case 3:
                print("#3: add airplane")
            case 4:
                print("#4: show airplanes")
            case 5:
                print("#5: add city")
            case 6:
                print("#6: show cities")
            case 7:
                print("#7: add flight")
            case 8:
                print("#8: show flights")
            