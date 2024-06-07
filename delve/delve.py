import matplotlib
import datamapplot
import numpy as np
import io

from sow.util import patch_aspect_ratio

from pandas import read_csv
d = read_csv("delve_train1_2_test1_points_label0.csv", header=None)
word_data = d.values
word_data = patch_aspect_ratio(word_data, 11/10, 'delve_train1_2_test1_render10b_extent.json')

f = open("delve_all_test_filtered.txt", "r")
lines = f.readlines()
word_labels = np.array(lines)

fig, ax = datamapplot.create_plot(word_data)

fig.savefig("delve_plot.png", bbox_inches="tight")

plot = datamapplot.create_interactive_plot(
    word_data,
    hover_text = word_labels,
    font_family="Playfair Display SC",
)

plot.save("output.html")

# PYTHONPATH=.. python delve.py
# cp output.html index.html
# patch index.html index.patch

# diff -u output.html index.html > index.patch
