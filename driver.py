import car
import transport


def main_2():
    print('Inside main_2 func')
    car_ = car.Car(model='Tesla')
    car_.pollution_permit(20000)
    bike = car.Bike('Harley', 2019)
    bike.pollution_permit(200000)
    bike.play_with_pandas()
    tractor_pollution_permit = transport.TractorPollutionPermit()
    tractor_pollution_permit.fetch_tractor(2018, True)
    tractor_pesticides = transport.TractorPesticides()
    tractor_pesticides.fetch_pesticides_permit(11)
