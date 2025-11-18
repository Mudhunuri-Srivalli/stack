from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, price, is_available=True):
        self._vehicle_id = vehicle_id        # Private attribute
        self._brand = brand                  # Private attribute
        self._price = price                  # Private attribute
        self._is_available = is_available    # Private attribute

    # Getter for brand
    def get_brand(self):
        return self._brand

    # Getter for price
    def get_price(self):
        return self._price

    # Getter for availability
    def is_available(self):
        return self._is_available

    # Setter for price
    def set_price(self, new_price):
        self._price = new_price

    # Setter for availability
    def set_availability(self, status):
        self._is_available = status

    # Abstract method to get details
    @abstractmethod
    def get_details(self):
        pass

    # Abstract method to calculate cost based on days
    @abstractmethod
    def calculate_cost(self, days):
        pass
