# `cutout`
Survey cutouts plotted directly. 

No user choices, just plotting! These cutouts are intended to be used for a quick view, not analysis.

## Installation

To install:
```bash
cd ~

git clone https://github.com/avapolzin/cutout.git

cd cutout

sudo pip install .

````
or 
```bash
pip install cutout
```

## Getting Started

**`cutout` is intended to be as simple to use as possible.** The primary, and only necessary, input is an object's name or coordinates. 

It is also possible to toggle whether a WCS grid, scalebar, and/or object label is shown, and where/whether to save an output image file. Defaults are no WCS grid, scalebar, or object label, and the output is only shown, not saved locally.

A few examples:
```python
import cutout

cutout.survey.decals('Leo P', wcsgrid = False, scalebar = False, 
	savepath = 'leop_cutout.png', labelimg = True)

cutout.survey.decals('10:21:45.12 +18:05:16.89', wcsgrid = False, scalebar = False, 
	savepath = 'leop_cutout.png')

cutout.survey.hscssp('COSMOS-dw1')

cutout.survey.panstarrs('NGC 5486')
```

All other choices, like cutout size/FOV, effective pixel scale, image scaling etc. are hardcoded and not user-facing. This is done to keep the code's use quick and painless.

Survey options to now are DECaLS (`decals`), HSC-SSP (`hscssp`), and Pan-STARRS (`panstarrs`). To request other surveys be added, please open an issue and link to the image retrieval instructions for that survey. (HSC-SSP data access requires an account, the credentials of which can be passed to the cutout server following [these instructions](https://github.com/dr-guangtou/unagi/blob/master/demo/demo_hsc_config.ipynb).)

Note that HTTPS errors may occur if a survey's cutout server is down or unreachable for any reason.

(If there is sufficient interest, I may add the ability to rotate cutouts freely and show multiple cutouts simultaneously. This increases the complexity of the user input, so to keep the top level functions as simple as possible, these features are not included for now.)

## Citation

If you use this package or the scripts in this repository in a publication, please add a footnote linking to https://github.com/avapolzin/cutout and/or consider adding this software to your acknowledgments. If you would like to cite `cutout`, please use the Zenodo DOI linked [here]().