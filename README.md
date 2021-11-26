[![maintained by dataroots](https://img.shields.io/badge/maintained%20by-dataroots-%2300b189)](https://dataroots.io)
 ![](https://media-exp1.licdn.com/dms/image/C4D1BAQFJFecNiY6xNA/company-background_10000/0/1606894615032?e=1628604000&v=beta&t=hNYzs9y3EA-620Ck8ip1QaZc77eXlH1ZUl-E-sLI6wo "Logo")
[![PyPI](https://img.shields.io/badge/PyPI-0.1.7-orange.svg)](https://test.pypi.org/project/rootsstyle/)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/downloads/)
[![codecov](https://codecov.io/gh/datarootsio/rootsstyle/branch/main/graph/badge.svg?token=4agmmGuhtu)](https://codecov.io/gh/datarootsio/rootsstyle)


# rootsstyle

A dataroots inspired style for Matplotlib. Works with any visualization tools that builds upon Matplotlib (seaborn, pandas).

<div align="center">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/examples.png?token=AKP7KEG5WOE2WQF4XBGEE33BVCBNK">
</div>


## Installation

```
pip install -i https://test.pypi.org/simple/ rootsstyle
```

## Usage

```python
import rootsstyle
import matplotlib.pyplot as plt

# globally
plt.style.use(rootsstyle.style)

# within context manager
with plt.style.context(rootsstyle.style):
    # ...
```

```python
#More functionalities
'Place the legend to the left of the graph': rootsstyle.legend()
'Horizontal label of y-axis above the yaxis': rootsstyle.ylabel()
```

## Color Palette
<div align="center">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/palette.png?token=AKP7KEES4YKJJGD4MABU633BU42ZQ" style="height: 550px;">
</div>


## ROADMAP
### v0.1.7
- Add Changelogs.txt
- Add green-to-blue and blue-to-green gradients
- rootsstyle.barplot_show_values: shows values in bars and (optionally) removes y-axis
- Formatting of x-tick labels so that there is no overlap (rotate if necessary)
### v0.1.X
- Open-source
  - Cleanup repository
  - Update image-src in README
  - Publish to PyPi instead of Test PyPi
- rootsstyle.publish(): allows you to publish an example .png with the corresponding code sample
- rootsstyle.data_label(): labels a specific datapoint with some text
