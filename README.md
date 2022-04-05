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

To add a new inlet, simply add a new entry to `_data/inlets.yml` for the inlet and make sure all the relevant figures are present and up-to-date.
Entries are defined as follows:

- id: the identifier used for the inlet. Will be used to generate its name as well, which is assumed to be the id with all `"-"` characters replaced with `" "`, and the remaining words capitalized. For example, the id `saanich-inlet` uses the name `Saanich Inlet`.
- length: the length of the inlet
- depth: the maximum depth of the inlet
- basins: a description of the number of basins in the inlet, and where they are
- sill: a description of the sill depth for the inlet
- surface: the surface area of the inlet
- runoff: a series of paragraphs describing the runoff process for the inlet
- renewal: a series of paragraphs describing the deep water renewal process for the inlet
- legacy: a flag to indicate whether to use the old-style map and section plot combined into one image, or a newer version with two separate images. `true` means to use the old style

`length`, `depth`, `basins`, `sill`, `surface`, `runoff`, and `renewal` are all optional, and their sections will not show up if they aren't defined.
`legacy` defaults to `false` if it is not present.

Once the inlet has been defined in `_data/inlets.yml`, a new tab will be generated using that information which will look for the following images in the `figures/` directory:
- `<id>-samples.png`: the sampling histogram
- `<id>-monthly-sampling.png`: the sampling heatmap
- `<id>-map.gif` if `legacy` is `true`: the combined map and section plot
- `<id>-map.png` and `<id>-section.png` if `legacy` is `false` or not defined: the map and section plots
- `<id>-temperature.png`: the time series plot of temperature in the inlet, to be displayed when "Raw Data" is selected
- `<id>-salinity.png`: the time series plot of salinity in the inlet, to be displayed when "Raw Data" is selected
- `<id>-oxygen.png`: the time series plot of dissolved oxygen in the inlet, to be displayed when "Raw Data" is selected
- `<id>-temperature-average.png`: the time series plot of temperature in the inlet, to be displayed when "Monthly Averaged Time Series" is selected
- `<id>-salinity-average.png`: the time series plot of salinity in the inlet, to be displayed when "Monthly Averaged Time Series" is selected
- `<id>-oxygen-average.png`: the time series plot of dissolved oxygen in the inlet, to be displayed when "Monthly Averaged Time Series" is selected

You should also ensure that the relevant annual averages and anomalies plots are up to date with the data from the new inlet included.
