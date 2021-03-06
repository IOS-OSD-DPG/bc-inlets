#!/usr/bin/env python

import argparse
from dataclasses import dataclass
import json
import os
import requests
from typing import List

import matplotlib.pyplot as plt

params = {
    "logo": "false",
    "access_token": "pk.eyJ1IjoiY3lib3Jnc3BoaW54IiwiYSI6ImNsMDJweTU5MTAxemozY3F4N3psem44Mm8ifQ.BCyXz0gxpY2MhF42Om1cjQ",
}

@dataclass
class Inlet:
    name: str
    dimensions: str
    boundaries: List[float]

maps = [
    Inlet(boundaries=[-123.7, 48.4, -123.2, 48.8], dimensions="500x700", name="Saanich Inlet"),
    Inlet(boundaries=[-129.3, 53.3, -128.5, 54.1], dimensions="500x700", name="Douglas Channel"),
    Inlet(boundaries=[-123.3, 49.2, -122.8, 49.5], dimensions="600x600", name="Indian Arm"),
    Inlet(boundaries=[-127.5, 52.3, -126.7, 53.0], dimensions="500x700", name="Dean Channel"),
    Inlet(boundaries=[-125.0, 50.3, -124.1, 50.4], dimensions="500x400", name="Toba Inlet"),
    Inlet(boundaries=[-125.3, 50.2, -124.6, 51.0], dimensions="500x700", name="Bute Inlet"),
    Inlet(boundaries=[-127.9, 51.8, -127.2, 52.4], dimensions="600x600", name="Burke Channel"),
    Inlet(boundaries=[-130.2, 54.8, -129.7, 55.4], dimensions="500x700", name="Observatory Inlet"),
    Inlet(boundaries=[-126.7, 49.5, -126.0, 49.7], dimensions="700x400", name="Muchalat Inlet"),
    Inlet(boundaries=[-123.4, 49.3, -123.2, 49.7], dimensions="500x700", name="Howe Sound"),
    Inlet(boundaries=[-125.1, 48.8, -124.6, 49.3], dimensions="500x700", name="Alberni Inlet"),
    Inlet(boundaries=[-125.3, 48.9, -125.0, 49.2], dimensions="500x500", name="Effingham Inlet"),
    Inlet(boundaries=[-128.1, 50.4, -127.5, 50.6], dimensions="700x500", name="Quatsino Sound"),
    Inlet(boundaries=[-124.4, 49.6, -123.5, 50.3], dimensions="600x700", name="Jervis Inlet"),
    Inlet(boundaries=[-131.8, 52.4, -131.0, 53.0], dimensions="600x600", name="Juan Perez Sound"),
    Inlet(boundaries=[-126.8, 50.4, -125.4, 51.2], dimensions="600x600", name="Knight Inlet"),
    Inlet(boundaries=[-127.9, 51.3, -126.5, 51.9], dimensions="700x500", name="Rivers Inlet"),
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

def main(inlet, only_update):
    if not only_update and inlet == "all":
        get_map("cl0cpnth0000d15rujrameamv", "-126,51.9,5.4", "900x700", "all inlets")

    for mapbox in maps:
        if inlet == "all" or inlet == mapbox.name:
            if not only_update:
                get_map("cl1gtkgu6002i14rt1l9kxo5w", mapbox.boundaries, mapbox.dimensions, mapbox.name, True)
            add_axes(mapbox.name, mapbox.boundaries, mapbox.dimensions)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inlet", type=str, nargs="?", default="all")
    parser.add_argument("--update", action="store_true")
    args = parser.parse_args()
    main(args.inlet, args.inlet)
