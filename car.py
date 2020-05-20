from vehicles import Vehicle, Dummy
from transport import CarPollutionPermit, BikePollutionPermit
import pandas as pd


class Car(Vehicle):
    def __init__(self, model, year=2015, capacity=30):
        self.model = model
        self.year = year
        self.capacity = capacity
        self.pollution_compliance = False

    def pollution_permit(self, distance):
        mileage = self.mileage_calculator(distance, self.capacity)
        car_pollution = CarPollutionPermit()
        self.pollution_compliance = car_pollution.check_permit(
            self.year, mileage)
        print(self.pollution_compliance)


class Bike(Vehicle, BikePollutionPermit, Dummy):
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.capacity = 100
        self.pollution_compliance = True
        self.car_pollution_permit = CarPollutionPermit()

    def pollution_permit(self, distance):
        mileage = self.mileage_calculator(distance, self.capacity)
        self.pollution_compliance = self.check_permit(
            self.year, mileage)
        print(self.pollution_compliance)

    def play_with_pandas(self):
        df = pd.DataFrame([1, 2, 3, 4])
        print("The dataframe is: ")
        print(df)
