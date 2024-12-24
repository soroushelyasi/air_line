import os.path


class Storage:
    def __init__(self):
        self.GENERAL_STORAGE_ADDRESS = "./storage/"
        self.AIRPLANES_ADDRESS = self.GENERAL_STORAGE_ADDRESS+"airplanes.json"
        self.CITIES_ADDRESS = self.GENERAL_STORAGE_ADDRESS+"cities.json"
        self.FLIGHTS_ADDRESS = self.GENERAL_STORAGE_ADDRESS+"flights.json"
        self.PASSENGERS_ADDRESS = self.GENERAL_STORAGE_ADDRESS+"passengers.json"
        self.airplanes = self.fetch_data(self.AIRPLANES_ADDRESS)
        self.cities = self.fetch_data(self.CITIES_ADDRESS)
        self.flights = self.fetch_data(self.FLIGHTS_ADDRESS)
        self.passengers = self.fetch_data(self.PASSENGERS_ADDRESS)

    def add_airplane(self, airplane):
        self.airplanes.append(airplane)

    def add_city(self, city):
        self.cities.append(city)

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def get_airplane(self, name):
        items = [e for e in self.airplanes if e.name == name]
        if len(items) > 0:
            return items[0]
        else:
            return None

    def get_all_airplanes(self):
        return self.airplanes

    def get_city(self, name):
        items = [e for e in self.cities if e.name == name]
        if len(items) > 0:
            return items[0]
        else:
            return None

    def get_all_cities(self):
        return self.cities

    def get_flight(self, flight_number):
        items = [e for e in self.flights if e.flight_number == flight_number]
        if len(items) > 0:
            return items[0]
        else:
            return None

    def get_all_flights(self):
        return self.flights

    def get_passenger(self, passport_id):
        items = [e for e in self.passengers if e.passport_id == passport_id]
        if len(items) > 0:
            return items[0]
        else:
            return None

    def get_all_passengers(self):
        return self.passengers

    def fetch_data(self, storage_address):
        if os.path.isfile(storage_address):
            return []
        else:
            return []
