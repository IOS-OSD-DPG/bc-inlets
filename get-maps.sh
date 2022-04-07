#!/bin/sh

DATA="logo=false&access_token=pk.eyJ1IjoiY3lib3Jnc3BoaW54IiwiYSI6ImNsMDJweTU5MTAxemozY3F4N3psem44Mm8ifQ.BCyXz0gxpY2MhF42Om1cjQ"
curl -g "https://api.mapbox.com/styles/v1/cyborgsphinx/cl0cpnth0000d15rujrameamv/static/-126,51.4,5.7/900x700?$DATA" --output figures/all-inlets-map.png
curl -g "https://api.mapbox.com/styles/v1/cyborgsphinx/cl1gtkgu6002i14rt1l9kxo5w/static/[-129.25,53.35,-128.9,53.85]/500x700?$DATA" --output figures/douglas-channel-map.png
