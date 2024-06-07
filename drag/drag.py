import matplotlib
import datamapplot
import numpy as np
import io

from sow.util import patch_aspect_ratio

from pandas import read_csv
d = read_csv("drag_train1_0_test1_points_label0.csv", header=None)
word_data = d.values
word_data = patch_aspect_ratio(word_data, 11/10, 'drag_train1_4_test1_render10b_extent.json')

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

