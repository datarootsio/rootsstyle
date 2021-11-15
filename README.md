[![maintained by dataroots](https://img.shields.io/badge/maintained%20by-dataroots-%2300b189)](https://dataroots.io)
 ![](https://media-exp1.licdn.com/dms/image/C4D1BAQFJFecNiY6xNA/company-background_10000/0/1606894615032?e=1628604000&v=beta&t=hNYzs9y3EA-620Ck8ip1QaZc77eXlH1ZUl-E-sLI6wo "Logo")
[![PyPI](https://img.shields.io/badge/PyPI-0.1.2-orange.svg)](https://test.pypi.org/project/rootsstyle/)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20-blue.svg)](https://www.python.org/downloads/)
[![codecov](https://codecov.io/gh/datarootsio/rootsstyle/branch/main/graph/badge.svg?token=4agmmGuhtu)](https://codecov.io/gh/datarootsio/rootsstyle)


# rootsstyle

A dataroots inspired style for Matplotlib. Works with any visualization tools that builds upon Matplotlib (seaborn, pandas).

<div style="display: flex;">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/scatterplot.png?token=AKP7KEELTENS6ATFY7DGBJ3BTN6PI" style="height: 300px;">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/barplot_tips.png?token=AKP7KEGHGVGHU6EAXBAMEKDBTN6N2" style="height: 300px;">
    
</div>
<div style="display: flex;">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/lineplot.png?token=AKP7KEEIUJKJSOHXIXJYL3TBTOARI" style="height: 300px;">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/violinplot.png?token=AKP7KEHBIIMAROVSLTIWYHLBTN6P6" style="height: 300px;">
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

## Color Palette
<div align="center">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/palette.png?token=AKP7KEEQA3IL6WAW655CMKLBTPBFG" style="height: 550px;">
</div>


## TODO

### VISUALS
- Add more colors
- barplots: add values in bars + remove y-axis
