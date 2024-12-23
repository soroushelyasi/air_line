from passenger import Passenger
from city import City
from flight import Flight
from airplane import Airplane
from storage import Storage

if __name__ == '__main__':
    stg = Storage()
    # Make a game instance, and run the game.
    print("Welcome to airline!!!")
    while True:
        print("#1: Add passenger")
        print("#2: Show passengers")
        print("#3: Add airplane")
        print("#4: Show airplanes")
        print("#5: Add city")
        print("#6: Show cities")
        # print("#7: Add flight")
        # print("#8: Show flights")
        selected_action = int(input("select an action number: "))
        match selected_action:
            case 1:
                new_passenger = Passenger(
                    input("Passenger name:").upper().strip(),
                    input("Passenger passport ID:").upper().strip())
                stg.add_passenger(new_passenger)
                print(stg.get_passenger(new_passenger.passport_id).name)
            case 2:
                print("passengers are")
                for i in stg.get_all_passengers():
                    print("name: "+i.name +
                          "\t\t***\t\tpassport ID: " + i.passport_id)
            case 3:
                new_airplane = Airplane(
                    input("Airplane name:").upper().strip(),
                    input("Airplane class:").upper().strip(),
                    int(input("Number of passengers:").strip()))
                stg.add_airplane(new_airplane)
                print(stg.get_airplane(new_airplane.name).airplane_class)
            case 4:
                print("passengers are")
                for i in stg.get_all_airplanes():
                    print("name: "+i.name +
                          "\t\t***\t\tclass: " + i.airplane_class,
                          "\t\t***\t\tnumber of passengers: " + str(i.number_of_passengers))
            case 5:
                new_city = City(
                    input("City name:").upper().strip(),
                    int(input("City longitude:").strip()),
                    int(input("City latitude:").strip()))
                stg.add_city(new_city)
                print(stg.get_city(new_city.name).longitude)
            case 6:
                print("cities are")
                for i in stg.get_all_airplanes():
                    print("name: "+i.name +
                          "\t\t***\t\longitude: " +  str(i.longitude),
                          "\t\t***\t\tlatitude " + str(i.latitude))
            # case 7:
            #     new_flight = Flight(
            #         int(input("Flight number:").strip()),
            #         input("Flight airplane name:").upper().strip(),
            #         input("Flight city name from:").upper().strip(),
            #         input("Flight city name to:").upper().strip(),
            #         int(input("Flight number of stops:").strip()),
            #         "",
            #         int(input("Flight set of passengers:").strip()),
            #     )
            #     for i in range(new_flight.number_of_stops):
            #         new_flight.list_of_city_for_stop_in_order += input(
            #             "+#"+i+": Flight stop city  in order:").upper().strip()
            #     stg.add_flight(new_flight)
            #     print(stg.get_flight(new_flight.flight_number).name)
            # case 8:
            #     print("#8: show flights")
            case default:
                print("not supported")