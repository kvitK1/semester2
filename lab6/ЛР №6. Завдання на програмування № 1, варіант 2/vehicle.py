"""lab5 2var task1"""


class Vehicle:
    """A class to represent a vehicle and info about it.

    Attributes
    ------------
        brand: str
            brand of the vehicle
        model: str
            model of the vehicle
        m_type: str
            model type of the vehicle
        gas_tank_size: int
            volume of gas tank size
        fuel_consum: 6|int
            fuel consumation per 100km of distance (default to 6)
        fuel_level: 0|int
            number of fuel level (default to 0)

    """

    def __init__(self, brand, model, m_type, gas_tank_size,
    fuel_consum=6, fuel_level=0):
        """Inits the Vehicle class with brand, model, m_type, gas_tank_size,
            fuel_consum, fuel_level."""
        self.brand = brand
        self.model = model
        self.m_type = m_type
        self.gas_tank_size = gas_tank_size
        self.fuel_level = fuel_level
        self.fuel_consum = fuel_consum

    def __str__(self):
        """Shows the information about vehicle when printed."""
        return f"Vehicle {self.brand} {self.model} is a {self.m_type}. \
It has a gas tank size of {self.gas_tank_size}."

    def fuel_up(self, fuel):
        """Increases the fuel level.
            Returns the info about being filled."""
        if fuel >= 0:
            self.fuel_level += fuel
            if self.fuel_level > self.gas_tank_size:
                self.fuel_level = self.gas_tank_size
        return "Gas tank is filled."

    def get_fuel_level(self):
        """Returns the fuel level."""
        return self.fuel_level

    def drive(self, distance):
        """Counts the fuel consumption per certain distance.
            Reduces the fuel level."""
        fuel_costs = int(distance*self.fuel_consum/100)
        if fuel_costs > self.fuel_level:
            return "Not enough fuel level in a gas tank."
        self.fuel_level -= fuel_costs
        return f"The {self.brand} {self.model} is now driving."

class ElectricVehicle(Vehicle):
    """A class to represent an electrovehicle and info about it.

    Attributes
    ------------
        brand: str
            brand of the electrovehicle
        model: str
            model of the electrovehicle
        m_type: str
            model type of the electrovehicle
        fuel_level: 0|int
            number of fuel level (default to 0)
        battery: Battery
            battery of the electrovehicle

    """
    def __init__(self, brand, model, m_type, fuel_level=0):
        """Inits the ElectroVehicle class with brand, model, m_type, fuel_level."""
        super().__init__(brand, model, m_type, fuel_level)
        self.battery = Battery()

    def __str__(self):
        """Shows the information about electrovehicle when printed."""
        return f"Vehicle {self.brand} {self.model} is a {self.m_type}."

    def charge(self):
        """Charges battery of electrovehicle to 100%."""
        self.battery.charge_level = 100
        return "The vehicle is fully charged."

    def get_charge_level(self):
        """Shows the level of battery charge."""
        return self.battery.charge_level

    def drive(self):
        """Electrovehicle drives and battery discharges."""
        self.battery.charge_level = 0
        return f"The {self.brand} {self.model} is now driving."

    def get_battery_info(self):
        """Shows information about the battery."""
        return f"Battery has size of {self.battery.size}, \
it is charged up to {self.battery.charge_level}%"

class Battery:
    """A class to represent a battery and info about it.

    Attributes
    ------------
        size: 85|int
            size of the battery (default to 85)
        charge_level: 0|int
            charge level of the battery (default to 0)

    """

    def __init__(self, size=85, charge_level=0):
        """Inits the Battery class with size and charge_level."""
        self.size = size
        self.charge_level = charge_level


def test_vehicle():
    """
    Test function
    """
    print("Testing Vehicle classes...")
    # A basic Vehicle has a brand, model, type, volume of gas_tank_size
    # fuel_level that by default equals 0 and fuel_consumption
    # that by default equals 6. It can drive and be fueled up
    vehicle = Vehicle("Subaru", "Forester", "Crossover", 16, 7)
    assert (type(vehicle) == Vehicle)
    assert (isinstance(vehicle, Vehicle))
    assert (str(vehicle) == "Vehicle Subaru Forester is a Crossover. It has a gas tank size of 16.")

    # change some attributes
    assert (vehicle.fuel_up(12) == "Gas tank is filled.")
    assert (vehicle.get_fuel_level() == 12)
    # When vehicle drives, it uses the fuel level
    # Vehicle uses fuel in amount of
    # fuel_consumption * distance to drive / 100
    assert (vehicle.drive(100) == "The Subaru Forester is now driving.")
    # the vehicle travelled 100 km and the fuel level reduced
    # from 12 to 5
    assert (vehicle.get_fuel_level() == 5)
    assert (vehicle.drive(100) == "Not enough fuel level in a gas tank.")

    # ElectricVehicle is a Vehicle that doesn't need a gas_tank_size
    # and doesn't have a fuel_consumption.
    # You can charge and drive it.
    electric_vehicle = ElectricVehicle('Tesla', 'Model 3', 'Sedan')
    assert (type(electric_vehicle) == ElectricVehicle)
    assert (isinstance(electric_vehicle, ElectricVehicle))
    assert (isinstance(electric_vehicle, Vehicle))
    assert (str(electric_vehicle) == "Vehicle Tesla Model 3 is a Sedan.")

    assert (electric_vehicle.get_fuel_level() == 0)
    assert (electric_vehicle.charge() == "The vehicle is fully charged.")
    assert (electric_vehicle.get_charge_level() == 100)
    assert (electric_vehicle.drive() == "The Tesla Model 3 is now driving.")
    assert (electric_vehicle.get_charge_level() == 0)

    # the attribute battery has to belong to Battery class
    # the Battery has a size, that by default equals 85
    # and charge level that by default equals 0
    assert (type(electric_vehicle.battery) == Battery)
    assert (isinstance(electric_vehicle.battery, Battery))
    assert (electric_vehicle.get_battery_info() == "Battery has size of 85, it is charged up to 0%")

    print("Done!")


if __name__ == '__main__':
    test_vehicle()
