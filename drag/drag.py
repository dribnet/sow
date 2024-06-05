# Ensure we don't generate large images for inline docs
# You probably want to remove this if running the notebook yourself
import matplotlib
# matplotlib.rcParams["figure.dpi"] = 72

import datamapplot

import numpy as np
import requests
import io

from pandas import read_csv
d = read_csv("drag_train1_0_test1_points_label0.csv", header=None)
word_data = d.values

f = open("drag_all_test_filtered.txt", "r")
lines = f.readlines()
word_labels = np.array(lines)

fig, ax = datamapplot.create_plot(word_data)

fig.savefig("drag_plot.png", bbox_inches="tight")

plot = datamapplot.create_interactive_plot(
    word_data,
    hover_text = word_labels,
    font_family="Playfair Display SC",
)

plot.save("output.html")

