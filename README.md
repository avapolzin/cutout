# `cutout`
Survey cutouts plotted directly. 

No user choices, just plotting! These cutouts are intended to be used for a quick view, not analysis.

## Installation



## Getting Started

**`cutout` is intended to be as simple to use as possible.** The primary, and only necessary, input is an object's name or coordinates. 

It is also possible to toggle whether a WCS grid, scalebar, and/or object label is shown, and where/whether to save an output image file. Defaults are no WCS grid, scalebar, or object label, and the output is only shown, not saved locally.

A few of examples:
```python
import cutout

cutout.survey.decals('M79', wcsgrid = False, scalebar = False, savepath = 'm79cutout.png', labelimg = True)

cutout.survey.decals('05:24:10.59 -24:31:27.3', wcsgrid = False, scalebar = False, 
	savepath = 'm79cutout.png', labelimg = False)

cutout.survey.hscssp('M79')
```

All other choices, like cutout size/FOV, effective pixel scale, image scaling etc. are hardcoded and not user-facing. This is done to keep the code's use quick and painless.

To request other surveys be added, please open an issue and link to the image retrieval instructions for that survey.

(If there is sufficient interest, I may add the ability to rotate cutouts freely and show multiple cutouts simultaneously. This increases the complexity of the user input, so to keep the top level functions as simple as possible, these features are not included for now.)

## Citation

If you use this package or the scripts in this repository in a publication, please add a footnote linking to https://github.com/avapolzin/cutout and/or consider adding this software to your acknowledgments. If you would like to cite `cutout`, please use the Zenodo DOI linked [here]().