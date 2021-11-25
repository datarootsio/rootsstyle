[![maintained by dataroots](https://img.shields.io/badge/maintained%20by-dataroots-%2300b189)](https://dataroots.io)
 ![](https://media-exp1.licdn.com/dms/image/C4D1BAQFJFecNiY6xNA/company-background_10000/0/1606894615032?e=1628604000&v=beta&t=hNYzs9y3EA-620Ck8ip1QaZc77eXlH1ZUl-E-sLI6wo "Logo")
[![PyPI](https://img.shields.io/badge/PyPI-0.1.6-orange.svg)](https://test.pypi.org/project/rootsstyle/)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/downloads/)
[![codecov](https://codecov.io/gh/datarootsio/rootsstyle/branch/main/graph/badge.svg?token=4agmmGuhtu)](https://codecov.io/gh/datarootsio/rootsstyle)


# rootsstyle

A dataroots inspired style for Matplotlib. Works with any visualization tools that builds upon Matplotlib (seaborn, pandas).

<div align="center">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/examples.png?token=AKP7KEHDACJ563AUQB4VMYDBTY5PC">
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
### VISUALS
- Fine tune colors
- barplots: add values in bars + remove y-axis
- Once public: reset image links in README to be readable in PyPI
