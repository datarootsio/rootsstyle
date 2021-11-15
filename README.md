[![maintained by dataroots](https://img.shields.io/badge/maintained%20by-dataroots-%2300b189)](https://dataroots.io)
 ![](https://media-exp1.licdn.com/dms/image/C4D1BAQFJFecNiY6xNA/company-background_10000/0/1606894615032?e=1628604000&v=beta&t=hNYzs9y3EA-620Ck8ip1QaZc77eXlH1ZUl-E-sLI6wo "Logo")
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
pip install -i https://test.pypi.org/simple/ rootsstyle==0.1.0
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

## TODO

### VISUALS
- Add more colors
- Legend for line graphs (next to lines)
- Display y-axis legend horizontal on top of axis (+readability)

### TECHNICALITIES
- Auto install matplotlib with package installation
- Add python badge to show which python versions are supported
- GitHub workflow to publish on pull-request



