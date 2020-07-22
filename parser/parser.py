def filter_currency_rates(currency_rates, currencies_to_filter):
    for date, rates in currency_rates.items():
        filtered_rates = {}
        for currency, value in rates.items():
            if currency in currencies_to_filter:
                filtered_rates[currency] = value
        currency_rates[date] = filtered_rates
    return currency_rates


def get_rates_by_date_range(date_rates=None, start_date=None, end_date=None):
    currency_rates = {}
    date_range = _get_date_range(start_date, end_date)
    for date, rates in date_rates.items():
        if date in date_range:
            currency_rates[date] = rates
    return currency_rates


def _get_date_range(start_date, end_date):
    date_range = [start_date]
    start_date_parsed = start_date.split("-")
    start_day = int(start_date_parsed[2])
    end_day = int(end_date.split("-")[2])
    day = start_day
    while day < end_day:
        day = day + 1
        new_date = [start_date_parsed[0].__str__(), start_date_parsed[1].__str__(), "{0:0=2d}".format(day)]
        date_range.append("-".join(new_date))
    return date_range
