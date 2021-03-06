[![dataroots](https://dataroots.io/maintained.svg)](https://dataroots.io/)
[![PyPI version](https://badge.fury.io/py/rootsstyle.svg)](https://badge.fury.io/py/rootsstyle)
[![Python Versions](https://img.shields.io/badge/python->=3.7,%20<3.10-blue.svg)](https://www.python.org/downloads/)
[![codecov](https://codecov.io/gh/datarootsio/rootsstyle/branch/main/graph/badge.svg?token=4agmmGuhtu)](https://codecov.io/gh/datarootsio/rootsstyle)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

<div align="center">

<img src="https://github.com/datarootsio/rootsstyle/blob/main/images/rootsstylelogo.png?raw=true" height="100px;">
</div>

A matplotlib styling package for clean, minimal dataroots themed plots. 
Works with any visualization tools that builds upon Matplotlib (seaborn, pandas).

<img align="center" src="https://github.com/datarootsio/rootsstyle/blob/main/images/examples.png?raw=true">



# Installation
### using [pip](https://pypi.org/)
```python
pip install rootsstyle
```
### using [poetry](https://python-poetry.org/)
```python
poetry add rootsstyle
```

# Usage
**Examples**

<a href="https://colab.research.google.com/drive/1kn7YLDR4hqI9GVzeiRH9aQTEeS7HPrw7" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>

<table width="100%">
<tr>
<td width="50%"> 

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
<td width="50%"> 

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
<td width="50%"><img src="https://github.com/datarootsio/rootsstyle/blob/main/images/example_lineplot.png?raw=true"></td>
<td width="50%"> <img src="https://github.com/datarootsio/rootsstyle/blob/main/images/example_barplot.png?raw=true"></td>
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
* Place the legend to the right of the plot.<br>For lineplots, place the legend entries right of the corresponding line.
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
<table width="100%">
    <tr>
        <td width="40%" align="center">The color palettes are added to the global matplotlib color registry. You can thus easily use a palette by simply providing the name in the correct location.</td>
        <td width="60%" align="center">
            <img src="https://github.com/datarootsio/rootsstyle/blob/main/images/palette.png?raw=true" height="350px;">
        </td>
    </tr>
</table>


# VERSIONING

A [semantic versioning](https://semver.org/) scheme is used to update the version on the commit messages. This happens automatically on any push to the main branch. Only patches, minor and major changes will generate a tag, release and publishing of the package. We stick to the default [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). To use this system, commit messages should adhere to a couple of rules:

1. Commits must follow the following syntax

    ```
    <type>(<scope>): <subject>
    <BLANK LINE>
    <body>
    <BLANK LINE>
    <footer>
    ```

2. Type should be one of the following:
    * feat: A new feature
    * fix: A bug fix
    * docs: Documentation only changes
    * style: Changes that do not affect the meaning of the code (formatting, missing semi-colons, etc)
    * refactor: A code change that neither fixes a bug nor adds a feature
    * perf: A code change that improves performance
    * test: Adding missing or correcting existing tests
    * chore: Changes to the build process or auxiliary tools and libraries such as documentation generation

3. Body (optional) is used to motivate the change
4. Footer (optional) is used to link to any **issues** that the commit closes and for **breaking changes**, in which case the line should start with `BREAKING CHANGE:`.

# CHANGELOG
The [CHANGELOG.md](https://github.com/datarootsio/rootsstyle/blob/main/CHANGELOG.md) file is automatically updated upon any new releases.

# License
This project is licensed under the terms of the MIT license.