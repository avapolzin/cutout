# `cutout`
Survey cutouts plotted directly. 

No user choices, just plotting! These cutouts are intended to be used for a quick view, not analysis.

## Installation



## Getting Started

**`cutout` is intended to be as simple to use as possible.** The primary, and only necessary, input is an object's name or coordinates. 

It is also possible to toggle rotation, whether a WCS grid and/or scalebar is shown, and where/whether to save an output image file. Defaults are no rotation, no WCS grid or scalenar, and the output is only shown not saved locally.

A few of examples:
```python
import giles

cutout.survey.decals('M79', rotation = None, wcsgrid = False, 
	scalebar = False, savepath = 'm79cutout.png')

cutout.survey.decals('05:24:10.59 -24:31:27.3', rotation = None, wcsgrid = False, 
	scalebar = False, savepath = 'm79cutout.png')

cutout.survey.hscssp('M79')
```

All other choices, like cutout size/FOV, effective pixel scale, image scaling etc. are hardcoded and not user-facing. This is done to keep the code's use quick and painless.

(If there is sufficient interest, I may add the ability to show multiple cutouts simultaneously. This increases the complexity of the user input, so to keep the top level functions as simple as possible, this feature is not included for now.)

## Citation

If you use this package or the scripts in this repository in a publication, please add a footnote linking to https://github.com/avapolzin/cutout and/or consider adding this software to your acknowledgments. If you would like to cite `cutout`, please use the Zenodo DOI linked [here]().