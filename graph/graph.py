# importing the required module
import matplotlib.pyplot as plt


def plot_graph(data):
    dates = []
    inr_rates = []
    gbp_rates = []
    for date, currency in data.items():
        dates.append(date)
        inr_rates.append(currency['INR'])
        gbp_rates.append(currency['GBP'])
    # plotting the points
    print(gbp_rates)
    plt.plot(dates, inr_rates)
    plt.plot(dates, gbp_rates)

    # naming the x axis
    plt.xlabel('date')
    # naming the y axis
    plt.ylabel('rate')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()
