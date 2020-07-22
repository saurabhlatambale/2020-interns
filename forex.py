import json

from graph.graph import plot_graph
from parser.parser import get_rates_by_date_range, filter_currency_rates

with open('data.json') as f:
    data = json.load(f)


def main():
    start_date = "2019-01-01"
    end_date = "2019-01-30"
    curreny_rates_filtered_by_date = get_rates_by_date_range(data['rates'], start_date, end_date)
    filter_currencies = ['INR', 'GBP']
    currency_rates_filtered_by_currency = filter_currency_rates(curreny_rates_filtered_by_date, filter_currencies)
    plot_graph(currency_rates_filtered_by_currency)


if __name__ == "__main__":
    main()
