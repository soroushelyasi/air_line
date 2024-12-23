import sys
from passenger import Passenger
from city import City
from flight import Flight
from airplane import Airplane

if __name__ == '__main__':
    # Make a game instance, and run the game.
    print("Welcome to airline!!!")
    while True:
        print("#1: Add passenger")
        print("#2: Show passengers")
        print("#3: Add airplane")
        print("#4: Show airplanes")
        print("#5: Add city")
        print("#6: Show cities")
        print("#7: Add flight")
        print("#8: Show flights")
        selected_action = int(input("select an action number: "))
        match selected_action:
            case 1:
                new_passenger = Passenger(
                    input("Passenger name:").upper().strip(),
                    input("Passenger passport ID:").upper().strip())
                print(new_passenger.name)
            case 2:
                print("#2: show passengers")
            case 3:
                new_airplane = Airplane(
                    input("Airplane name:").upper().strip(),
                    input("Airplane class:").upper().strip(),
                    int(input("Number of passengers:").strip()))
            case 4:
                print("#4: show airplanes")
            case 5:
                new_city = City(
                    input("City name:").upper().strip(),
                    int(input("City longitude:").strip()),
                    int(input("City latitude:").strip()))
            case 6:
                print("#6: show cities")
            case 7:
                new_flight = Flight(
                    int(input("Flight number:").strip()),
                    input("Flight airplane name:").upper().strip(),
                    input("Flight city name from:").upper().strip(),
                    input("Flight city name to:").upper().strip(),
                    int(input("Flight number of stops:").strip()),
                    "",
                    int(input("Flight set of passengers:").strip()),
                    )
                for i in range(new_flight.number_of_stops):
                    new_flight.list_of_city_for_stop_in_order+=input("+#"+i+": Flight stop city  in order:").upper().strip()
            case 8:
                print("#8: show flights")
