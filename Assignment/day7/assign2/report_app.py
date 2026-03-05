import time
from functools import wraps

# =========================
# DECORATORS
# =========================

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}")
        return result
    return wrapper

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {end - start:.4f} seconds")
        return result
    return wrapper

def validate_data(func):
    def wrapper(self, data, filename):
        if not data:
            raise ValueError("Report data cannot be empty!")
        return func(self, data, filename)
    return wrapper

# =========================
# CONTEXT MANAGER
# =========================

class ReportSaver:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("[INFO] Opening file...")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[INFO] Closing file...")
        self.file.close()

# =========================
# GENERATOR
# =========================

def data_generator(data):
    for item in data:
        yield item

# =========================
# BASE REPORT CLASS
# =========================

class Report:
    def format(self, record):
        raise NotImplementedError

    @log_action
    @measure_time
    @validate_data
    def generate(self, data, filename):
        with ReportSaver(filename) as file:
            for record in data_generator(data):
                file.write(self.format(record) + "\n")

# =========================
# REPORT TYPES
# =========================

class TextReport(Report):
    def format(self, record):
        return f"Record: {record}"

class CSVReport(Report):
    def format(self, record):
        return ",".join(str(x) for x in record)

# =========================
# CLIENT CODE
# =========================

if __name__ == "__main__":

    text_data = ["Alice", "Bob", "Charlie"]

    csv_data = [
        (1, "Laptop", 75000),
        (2, "Mouse", 500),
        (3, "Keyboard", 1500)
    ]

    print("\nGenerating Text Report...")
    TextReport().generate(text_data, "text_report.txt")

    print("\nGenerating CSV Report...")
    CSVReport().generate(csv_data, "sales_report.csv")