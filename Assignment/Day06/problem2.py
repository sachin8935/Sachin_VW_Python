from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    """
    Template Method Pattern:
    Defines the skeleton of report generation.
    """

    def generate_report(self):
        self.parse()
        self.validate()

        if self.requires_revalidation():
            self.revalidate()

        self.save()

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def revalidate(self):
        """Optional step (default does nothing)"""
        pass

    @abstractmethod
    def save(self):
        pass

    def requires_revalidation(self):
        """Hook method"""
        return False



class StandardReport(ReportGenerator):
    def validate(self):
        print("Validating standard report")



class SpecialReport(ReportGenerator):
    def requires_revalidation(self):
        return True

    def revalidate(self):
        print("Revalidating special report")


class PDFReport(StandardReport):
    def parse(self):
        print("Parsing PDF report")

    def save(self):
        print("Saving PDF report")


class DOCXReport(StandardReport):
    def parse(self):
        print("Parsing DOCX report")

    def save(self):
        print("Saving DOCX report")


class TXTReport(StandardReport):
    def parse(self):
        print("Parsing TXT report")

    def save(self):
        print("Saving TXT report")



class CSVReport(SpecialReport):
    def parse(self):
        print("Parsing CSV report")

    def validate(self):
        print("Validating CSV report")

    def save(self):
        print("Saving CSV report")


class JSONReport(SpecialReport):
    def parse(self):
        print("Parsing JSON report")

    def validate(self):
        print("Validating JSON report")

    def save(self):
        print("Saving JSON report")


def client_code(report: ReportGenerator):
    report.generate_report()
    print("-" * 40)


if __name__ == "__main__":
    reports = [
        PDFReport(),
        DOCXReport(),
        TXTReport(),
        CSVReport(),
        JSONReport()
    ]

    for r in reports:
        client_code(r)
