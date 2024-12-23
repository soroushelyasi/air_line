import os.path


class Storage:
    def __init__(self):
        self.general_storage_address = "./storage/"
        self.airplanes = self.fetch_airplanes()
        self.cities = self.fetch_cities()
        self.flights = self.fetch_flights()
        self.passengers = self.fetch_passengers()

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

    def fetch_airplanes(self):
        storage_address = self.general_storage_address+"airplanes.json"
        if os.path.isfile(storage_address):
            return []
        else:
            return []

    def fetch_cities(self):
        storage_address = self.general_storage_address+"cities.json"
        if os.path.isfile(storage_address):
            return []
        else:
            return []

    def fetch_flights(self):
        storage_address = self.general_storage_address+"flights.json"
        if os.path.isfile(storage_address):
            return []
        else:
            return []

    def fetch_passengers(self):
        storage_address = self.general_storage_address+"passengers.json"
        if os.path.isfile(storage_address):
            return []
        else:
            return []
