
from abc import ABC
class Report(ABC):

    def generate(self):
        self.parse()
        self.validate()
        self.revalidate()
        self.save()

    def parse(self):
        print("Parsing data...")

    def validate(self):
        print("Validating data...")

    def revalidate(self):
        pass

    def save(self):
        print("Saving report...")