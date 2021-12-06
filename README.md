[![maintained by dataroots](https://img.shields.io/badge/maintained%20by-dataroots-%2300b189)](https://dataroots.io)
 ![](https://media-exp1.licdn.com/dms/image/C4D1BAQFJFecNiY6xNA/company-background_10000/0/1606894615032?e=1628604000&v=beta&t=hNYzs9y3EA-620Ck8ip1QaZc77eXlH1ZUl-E-sLI6wo "Logo")
[![PyPI version](https://badge.fury.io/py/rootsstyle.svg)](https://badge.fury.io/py/rootsstyle)
[![Python Versions](https://img.shields.io/badge/python->=3.7.1,%20<3.11-blue.svg)](https://www.python.org/downloads/)
[![codecov](https://codecov.io/gh/datarootsio/rootsstyle/branch/main/graph/badge.svg?token=4agmmGuhtu)](https://codecov.io/gh/datarootsio/rootsstyle)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

<div align="center">

# rootsstyle
</div>

A matplotlib styling package for clean, minimal dataroots themed plots. 
Works with any visualization tools that builds upon Matplotlib (seaborn, pandas).

<div align="center">
    <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/examples.png?token=AKP7KEHERXOOE7ETW64CLBTBW4TRE">
</div>



## Installation
### using pip
```python
pip install -i https://test.pypi.org/simple/ rootsstyle
```
### using [poetry](https://python-poetry.org/)
```python
# 1. Add repository to pyproject.toml
[[tool.poetry.source]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
# 2. Add package and automatically resolve dependencies
poetry add rootsstyle
```

## Usage
**Examples**

<a href="..." target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

<table>
<tr>
<td> 

```python
import rootsstyle
import matplotlib.pyplot as plt

plt.style.use(rootsstyle.style)
y, y2 = [3, 8, 1, 10], [8, 3, 10, 2]
plt.plot(y, label='y')
plt.plot(y2, label='y2', linestyle = 'dotted')
rootsstyle.ylabel('yvalues')
plt.xlabel('x-label')
rootsstyle.legend()
plt.title('Example plot')
plt.show()
```

</td>
<td> 

```python
import rootsstyle
import matplotlib.pyplot as plt

plt.style.use(rootsstyle.style)
languages = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
plt.bar(languages, students)
plt.xlabel('Language')
rootsstyle.show_bar_values()
plt.title('Example barplot')
plt.show()
```
</td>
</tr>
<tr>
<td><img src="images/example_lineplot.png"></td>
<td> <img src="images/example_barplot.png"></td>
</tr>
</table>


**STYLING**

```python
import rootsstyle
import matplotlib.pyplot as plt

# globally
plt.style.use(rootsstyle.style)

# within context manager
with plt.style.context(rootsstyle.style):
    # ...
```

**FUNCTIONS**
* Place the legend to the right of the plot.<br>For lineplots, place the legend entries left of the corresponding line.
    ```python 
    rootsstyle.legend(handles=None, labels=None, title=None)
    ```

* Place the y-label above the y-axis and rotate it, so that it is horizontal.
    ```python 
    rootsstyle.ylabel(ylabel: str)
    ```
* Show barvalues at each bar. <br>Removes the y-axis (optional).<br>Bar values can be shown just 'below' the top of each bar, or just 'above' each bar.
    ```python 
    rootsstyle.show_bar_values(remove_y_axis=True, fontsize=12, position="below", fmt="{:.0f}")
    ```

 

**COLOR PALETTE**
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="width: 50%; text-align: center;">
        <p>The color palettes are added to the global matplotlib color registry. You can thus easily use a palette by simply providing the name in the correct location.</p>
    </div>
    <div>
        <img src="https://raw.githubusercontent.com/datarootsio/rootsstyle/main/images/palette.png?token=AKP7KEGUIHVYNEX4ZLD4LHLBW4TSQ" style="height: 350px;">
    </div>
</div>




## CHANGELOG
see the [CHANGELOG.md](https://github.com/datarootsio/rootsstyle/blob/main/CHANGELOG.md) file

## ROADMAP
### v0.2.0
- Automatic versioning with codacy github actions
- Automatic GH release with information from CHANGELOG.md 

### v1.0.0
- Public repo
- Github Page at datarootsio.github.io/rootsstyle
- Google Colab examples notebook

### v1.1.0
- <code>rootsstyle.publish()</code>: allows you to publish an example .png with the corresponding code sample for other users to utilize as an example plot.
