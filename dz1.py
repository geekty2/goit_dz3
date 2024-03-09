from datetime import datetime, date

def days_difference(date_str):
    try:
        given_date = date.fromisoformat(date_str)
        today = date.today()
        days_diff = (today - given_date).days
    except ValueError:
        days_diff = None

    return days_diff

given_date = "2024-01-21"
days_diff = days_difference(given_date)

if days_diff is None:
    print("Невірний формат дати.")
else:
    print(f"Кількість днів: {days_diff}")
