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

`length`, `depth`, `basins`, `sill`, `surface`, `runoff`, and `renewal` are all optional, and their sections will not show up if they aren't defined.

Once the inlet has been defined in `_data/inlets.yml`, a new tab will be generated using that information which will look for the following images in the `figures/` directory:
- `<id>-samples.png`: the sampling histogram
- `<id>-monthly-sampling.png`: the sampling heatmap
- `<id>-map.png` and `<id>-section.png`: the map and section plots
- `<id>-temperature.png`: the time series plot of temperature in the inlet, to be displayed when "Raw Data" is selected
- `<id>-salinity.png`: the time series plot of salinity in the inlet, to be displayed when "Raw Data" is selected
- `<id>-oxygen.png`: the time series plot of dissolved oxygen in the inlet, to be displayed when "Raw Data" is selected
- `<id>-temperature-average.png`: the time series plot of temperature in the inlet, to be displayed when "Monthly Averaged Time Series" is selected
- `<id>-salinity-average.png`: the time series plot of salinity in the inlet, to be displayed when "Monthly Averaged Time Series" is selected
- `<id>-oxygen-average.png`: the time series plot of dissolved oxygen in the inlet, to be displayed when "Monthly Averaged Time Series" is selected

You should also ensure that the relevant annual averages and anomalies plots are up to date with the data from the new inlet included.

Viewing Changes Locally
-----------------------

The site is generated using [Jekyll](https://jekyll.com), which is the default static site generater for [GitHub Pages](https://pages.github.com).
Because the site is generated using templating, opening `index.html` directly in a browser is not going to produce great results, and will look nothing like the finished product.
In order to view your changes locally, you need to install Jekyll and then run `jekyll serve` from the root of the project (the same directory as this readme).
This will process the template and compile the site, and allow you to view it.

Running `jekyll serve` should result in something like the following:

	$ jekyll serve
	...
		Server address: http://127.0.0.1:4000
	  Server running... press ctrl-c to stop.

If you see this, just type `http://127.0.0.1:4000` into your browser and hit enter.

The images have recently been moved to another server to facilitate automated updating.
In order to view the images instead of broken links, you will need to do a few things:

1. Gather the relevant files into a single directory on your computer
1. Either move or link that directory to a subdirectory of this repository, e.g. `figures`
1. Change the `imageprefix` line in between the `---` lines at the top of `index.html` to the name of the subdirectory from the previous step
1. Run `jekyll serve` as described above

The site should now display the images properly.
