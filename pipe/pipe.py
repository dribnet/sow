# Ensure we don't generate large images for inline docs
# You probably want to remove this if running the notebook yourself
import matplotlib
# matplotlib.rcParams["figure.dpi"] = 72

import datamapplot

import numpy as np
import requests
import io

from sow.util import patch_aspect_ratio

from pandas import read_csv
the_csv = read_csv("lpipe_train1_2_test1_points_label0.csv", header=None)

word_data = the_csv.values
word_data = patch_aspect_ratio(word_data, 11/10, 'lpipe_train1_2_test3_render10b_extent.json')
# print(word_data[:5, :])

f = open("pipe_all_test_filtered.txt", "r")
lines = f.readlines()
word_labels = np.array(lines)

fig, ax = datamapplot.create_plot(word_data)

fig.savefig("pipe_plot.png", bbox_inches="tight")

plot = datamapplot.create_interactive_plot(
    word_data,
    hover_text = word_labels,
    font_family="Playfair Display SC",
)

plot.save("output.html")

