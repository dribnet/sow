import json

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
