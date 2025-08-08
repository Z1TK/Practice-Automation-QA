from faker import Faker
from datetime import date, timedelta

class Fake:
    
    def __init__(self, faker: Faker):
        self.facker = faker

    def date(self, start: timedelta = timedelta(days=-30), end: timedelta = timedelta()) -> date:
        return self.facker.date_between(start_date=start, end_date=end)
    
    def money(self, min: float = -100, max: float = 100) -> float:
        return self.facker.pyfloat(min_value=min, max_value=max)
    
    def category(self) -> str:
        return self.facker.random_element(['food', 'taxi', 'fuel', 'beauty', 'restaurants'])
    
    def sentence(self) -> str:
        return self.facker.sentence()
    
fake = Fake(faker=Faker())
