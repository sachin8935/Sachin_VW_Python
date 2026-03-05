from standard_report import StandardReport
from special_report import SpecialReport

class PDFReport(StandardReport):
    pass

class DOCXReport(StandardReport):
    pass

class TXTReport(StandardReport):
    pass


class CSVReport(SpecialReport):
    pass

class JSONReport(SpecialReport):
    pass
