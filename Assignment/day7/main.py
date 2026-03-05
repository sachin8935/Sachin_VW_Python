
from report_types import PDFReport, CSVReport

print("STANDARD REPORT:\n")
r1 = PDFReport()
r1.generate()

print("\nSPECIAL REPORT:\n")
r2 = CSVReport()
r2.generate()