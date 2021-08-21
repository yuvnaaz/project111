import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = []
for i in df["claps"].tolist():
    data.append(int(i))

mean = statistics.mean(data)
dev = statistics.stdev(data)

sample_means = []

for i in range(100):
    temp_ds = []
    for i in range(30):
        temp_ds.append(data[random.randint(0, len(data)-1)])
    sample_means.append(statistics.mean(temp_ds))

samp_mean = statistics.mean(sample_means)

dev1_strt, dev1_end = mean - dev, mean + dev
dev2_strt, dev2_end = mean - 2*dev, mean + 2*dev
dev3_strt, dev3_end = mean - 3*dev, mean + 3*dev

def plot_graph():
    fig = ff.create_distplot([sample_means], ["Samples"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.1], mode = 'lines', name = "MEAN"))
    fig.add_trace(go.Scatter(x = [dev1_strt, dev1_strt], y = [0, 0.1], mode = "lines", name = "STDEV 1 START"))
    fig.add_trace(go.Scatter(x = [dev1_end, dev1_end], y = [0, 0.1], mode = "lines", name = "STDEV 1 END"))
    fig.add_trace(go.Scatter(x = [dev2_strt, dev2_strt], y = [0, 0.1], mode = "lines", name = "STDEV 2 START"))
    fig.add_trace(go.Scatter(x = [dev2_end, dev2_end], y = [0, 0.1], mode = "lines", name = "STDEV 2 END"))
    fig.add_trace(go.Scatter(x = [dev3_strt, dev3_strt], y = [0, 0.1], mode = "lines", name = "STDEV 3 START"))
    fig.add_trace(go.Scatter(x = [dev3_end, dev3_end], y = [0, 0.1], mode = "lines", name = "STDEV 3 END"))
    fig.add_trace(go.Scatter(x = [samp_mean, samp_mean], y = [0, 0.1], mode = "lines", name = "SAMPLE MEAN"))
    print(f"The z score is:{(samp_mean - mean)/dev}")
    fig.show()

plot_graph()