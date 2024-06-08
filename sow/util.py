import json
import datamapplot
import numpy as np
from pandas import read_csv

# canonical interpolation function, like https://p5js.org/reference/#/p5/map
def map_number(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2;

def patch_aspect_ratio(data, target_aspect, json_file):
    with open(json_file) as f:
        d = json.load(f)
        x_extent = d[1][0] - d[0][0]
        y_extent = d[0][1] - d[1][1]
        aspect = x_extent/y_extent
        print(f"extent {x_extent} / {y_extent} = {aspect:5.2f}")

    if aspect < target_aspect:
        better_end_x = d[0][0] + (y_extent * 1.1)
        print(f"bounds: [{d[0][0]}, {d[1][1]}, {better_end_x}, {d[0][1]}]")
        data[:,0] = map_number(data[:,0], d[0][0], d[1][0], d[0][0], better_end_x)
    elif aspect > target_aspect:
        better_end_y = d[1][1] + (x_extent / 1.1)
        print(f"bounds: [{d[0][0]}, {d[1][1]}, {d[1][0]}, {better_end_y}]")
        data[:,1] = map_number(data[:,1], d[1][1], d[0][1], d[1][1], better_end_y)

    return data

def generate_web_page(word, word_points, word_extent, word_corpus):
    d = read_csv(word_points, header=None)
    word_data = d.values
    word_data = patch_aspect_ratio(word_data, 11/10, word_extent)

    f = open(word_corpus, "r")
    lines = f.readlines()
    word_labels = np.array(lines)

    fig, ax = datamapplot.create_plot(word_data)

    fig.savefig(f"{word}_plot.png", bbox_inches="tight")

    plot = datamapplot.create_interactive_plot(
        word_data,
        hover_text = word_labels,
        font_family="Playfair Display SC",
    )

    plot.save("output.html")
