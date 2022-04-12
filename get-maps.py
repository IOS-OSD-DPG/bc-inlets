#!/usr/bin/env python

import json
import os
import requests

import matplotlib.pyplot as plt

params = {
    "logo": "false",
    "access_token": "pk.eyJ1IjoiY3lib3Jnc3BoaW54IiwiYSI6ImNsMDJweTU5MTAxemozY3F4N3psem44Mm8ifQ.BCyXz0gxpY2MhF42Om1cjQ",
}

maps = [
    ([-123.7, 48.4, -123.2, 48.8], "500x700", "Saanich Inlet"),
    ([-129.3, 53.3, -128.5, 54.1], "500x700", "Douglas Channel"),
    ([-123.3, 49.2, -122.8, 49.5], "600x600", "Indian Arm"),
]

mapbox_url = "https://api.mapbox.com/styles/v1/cyborgsphinx/{}/static/{}/{}"

def file_name(name):
    return os.path.join("figures", name.lower().replace(" ", "-") + "-map.png")

def get_map(style, position, dimensions, name, extra_style=False):
    payload = params
    if extra_style:
        payload["setfilter"] = json.dumps(["==","name",name])
        payload["layer_id"] = "thalwegs"
    url = mapbox_url.format(style, position, dimensions)
    response = requests.get(url, stream=True, params=payload)
    if response.status_code == 200:
        filename = file_name(name)
        with open(filename, "wb") as f:
            for chunk in response:
                f.write(chunk)
    else:
        print("Could not get map for {}: {} {}".format(name, response.status_code, response.text))

def scale(min_val, max_val):
    return 1 if max_val - min_val < 6 else 2

def locations(min_val, max_val, length):
    stride = length // int(max_val - min_val)
    return [n for n in range(0, length + 1, stride * scale(min_val, max_val))]

def labels(min_val, max_val):
    return [n/10 for n in range(min_val, max_val + 1, scale(min_val, max_val))]

def add_axes(name, position, dimensions):
    x_len, y_len = dimensions.split("x")
    filename = file_name(name)
    with open(filename, "rb") as f:
        image = plt.imread(f)

    fig, ax = plt.subplots()
    ax.imshow(image)
    x_min, x_max = int(position[0] * 10), int(position[2] * 10)
    y_min, y_max = int(position[1] * 10), int(position[3] * 10)
    ax.set_xticks(
        locations(x_min, x_max, int(x_len)),
        labels(x_min, x_max),
    )
    ax.set_yticks(
        locations(y_min, y_max, int(y_len)),
        reversed(labels(y_min, y_max)),
    )

    dpi = fig.get_dpi()
    fig.set_size_inches(int(x_len) / dpi, int(y_len) / dpi)
    plt.tight_layout()
    plt.savefig(filename)

def main():
    get_map("cl0cpnth0000d15rujrameamv", "-126,51.4,5.7", "900x700", "all inlets")

    for mapbox in maps:
        get_map("cl1gtkgu6002i14rt1l9kxo5w", mapbox[0], mapbox[1], mapbox[2], True)
        add_axes(mapbox[2], mapbox[0], mapbox[1])

if __name__ == "__main__":
    main()
