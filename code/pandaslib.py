from datetime import datetime

def clean_currency(item: str) -> float:
    return float(str(item).replace('$', '').replace(',', ''))

def extract_year_mdy(timestamp):
     return datetime.strptime(timestamp, '%m/%d/%Y %H:%M:%S').year

def clean_country_usa(item: str) ->str:
     possibilities = [
        'united states of america', 'usa', 'us', 'united states', 'u.s.'
    ]
     if item.strip().lower() in possibilities:
        return 'United States'
     else:
        return item