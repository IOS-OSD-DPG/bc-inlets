BC Inlets
=========

This repo holds the website for the current version of the BC Inlets Program.
Go [here](https://ios-osd-dpg.github.io/bc-inlets/) to view the site in its current form.

Updating the Graphs
-------------------

Updating the graphs shown on the site is fairly simple: just replace the file in `figures/` that you want to update.
For example, if you want to update the raw temperature plot for Saanich Inlet, copy your new figure to `figures/saanich-inlet-temperature.png`.
To update the averaged version, copy the new image to `figures/saanich-inlet-temperature-average.png`.

Adding a New Inlet
------------------

Adding a new inlet should only require touching `index.html` and `figures/all-inlets-map.png`, the second of which is just to include the new inlet.

1. Add a button to the `inlet-choice` div. Make sure it has the `inlet-tablinks` class and an `onclick` property calling `changeInlet()` from `main.js`.
2. Add a section to the end with the class `inlet-content`, with an identifier matching the one in the `onclick` property of the button.
3. Add the name of the inlet to the section as a `h2` header.
4. Add a physical description and a map of the inlet.
5. Add two sections: one to hold the monthly average data, and the other to hold the raw data. Make sure the monthly average section has the classes `averaging-content` and `monthly`, and the raw data section has the classes `averaging-content` and `raw`.
6. Add the monthly averaged temperature, salinity, and dissolved oxygen figures to the monthly averaged section, and the raw temperature, salinity, and dissolved oxygen figures to the raw section.
7. Update the sampling history section in the `annual-averaging-content` div to include the new inlet's sampling history.
8. Update `figures/all-inlets-map.png` to include the new inlet, and make sure the associated description is up to date as well.

After all that, the new inlet should be viewable just like the others when its associated button is clicked.
Test it out locally to make sure it works, then commit the changes to the `main` branch and push to this repository.
It may take some time for GitHub Pages to update the website, so be patient.
