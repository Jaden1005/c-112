import statistics
import random
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
#mean = statistics.mean(data)fig = ff.create_distplot([data],["Math Score"],show_hist = False)
#fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Mean is:",mean)
print("Standard Deviation is:",stdev)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

mean_sample = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
z_score = (mean_sample - mean)/std_deviation
print("Mean is:",mean_sample)
print("Standard Deviation is:",std_deviation)
print("The z-score is = ",z_score)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.3], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 1.3], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1.3], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 1.3], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1.3], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,1.3], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,1.3], mode="lines", name="STANDARD DEVIATION 3 END"))
#fig.show()
#finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df = pd.read_csv("sample_2.csv")
data = df["reading_time"].tolist() 
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.3], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 1.3], mode="lines", name="MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1.3], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show()



