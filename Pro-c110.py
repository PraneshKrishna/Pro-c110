import plotly.figure_factory as ff
import statistics 
import random
import pandas as pd
import csv
import plotly.graph_objects as go


df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)

print("population mean:", population_mean)



def randomS(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean    


def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.show()


def setup():
    mean_list = []
    for i in range(0,100):
        means = randomS(30)
        mean_list.append(means)

    show_fig(mean_list)
    print("sampling mean: ",statistics.mean(mean_list))
    
setup()
