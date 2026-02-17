import time
from abc import ABC, abstractmethod
from datetime import datetime

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing {func.__name__} at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper


def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def validate_report(func):
    def wrapper(self, *args, **kwargs):
        if not self.report_name:
            raise ValueError("Report name cannot be empty")
        return func(self, *args, **kwargs)
    return wrapper


class ReportWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        print(f"[RESOURCE] Opening file {self.filename}")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[RESOURCE] Closing file {self.filename}")
        self.file.close()
        return False   




class Report(ABC):
    def __init__(self, report_name):
        self.report_name = report_name

    @abstractmethod
    def generate(self):
        """Generator that yields report content"""
        pass

    @log_execution
    @time_execution
    @validate_report
    def save(self, filename):
        with ReportWriter(filename) as file:
            for line in self.generate():   
                file.write(line + "\n")



class TextReport(Report):
    def __init__(self, report_name, data):
        super().__init__(report_name)
        self.data = data

    def generate(self):
        yield f"Report Name: {self.report_name}"
        yield "-" * 30
        for record in self.data:
            yield f"Record: {record}"


class StructuredReport(Report):
    def __init__(self, report_name, headers, rows):
        super().__init__(report_name)
        self.headers = headers
        self.rows = rows

    def generate(self):
        yield ",".join(self.headers)
        for row in self.rows:
            yield ",".join(map(str, row))


if __name__ == "__main__":
    text_data = ["Login successful", "File uploaded", "User logged out"]

    structured_headers = ["ID", "Name", "Salary"]
    structured_rows = [
        (1, "Sachin", 50000),
        (2, "Anita", 60000),
        (3, "Rahul", 55000)
    ]

    text_report = TextReport("System Logs", text_data)
    csv_report = StructuredReport("Employee Data", structured_headers, structured_rows)

    text_report.save("text_report.txt")
    csv_report.save("employee_report.csv")
