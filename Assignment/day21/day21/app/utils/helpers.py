def format_date(date):
    return date.strftime("%Y-%m-%d")

def calculate_age(birthdate):
    from datetime import datetime
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def generate_unique_id():
    import uuid
    return str(uuid.uuid4())