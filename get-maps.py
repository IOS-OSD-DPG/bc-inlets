#!/usr/bin/env python

import json
import os
import requests

params = {
    "logo": "false",
    "access_token": "pk.eyJ1IjoiY3lib3Jnc3BoaW54IiwiYSI6ImNsMDJweTU5MTAxemozY3F4N3psem44Mm8ifQ.BCyXz0gxpY2MhF42Om1cjQ",
}

maps = [
    ("-129,53.7,8.5", "500x700", "Douglas Channel")
]

mapbox_url = "https://api.mapbox.com/styles/v1/cyborgsphinx/{}/static/{}/{}"

def get_map(style, position, dimensions, name, extra_style=False):
    payload = params
    if extra_style:
        payload["setfilter"] = json.dumps(["==","name",name])
        payload["layer_id"] = "thalwegs"
    url = mapbox_url.format(style, position, dimensions)
    response = requests.get(url, stream=True, params=payload)
    if response.status_code == 200:
        filename = os.path.join("figures", name.lower().replace(" ", "-") + "-map.png")
        with open(filename, "wb") as f:
            for chunk in response:
                f.write(chunk)
    else:
        print("Could not get map for {}: {} {}".format(name, response.status_code, response.text))

def main():
    get_map("cl0cpnth0000d15rujrameamv", "-126,51.4,5.7", "900x700", "all inlets")

    for mapbox in maps:
        get_map("cl1gtkgu6002i14rt1l9kxo5w", mapbox[0], mapbox[1], mapbox[2], True)

if __name__ == "__main__":
    main()
