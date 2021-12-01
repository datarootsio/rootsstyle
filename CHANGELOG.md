<div align=center>
            <b>
            <p>========================</p>
            <p>2021-12-01   --   v0.1.8</p>
            <p>========================</p>
            </b>
        </div>

- updated CHANGELOG
- fixed branch misdirect in changelog GH actions
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-12-01   --   v0.1.8</p>
            <p>========================</p>
            </b>
        </div>

- script output update
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-12-01   --   v0.1.8</p>
            <p>========================</p>
            </b>
        </div>

- set default text color to textgray, added public colorlist as rootsstyle.colors, added example of data point label in scatterplot, added example of ytick rotation in heatmaps
- updated dataroots-green-to-blue palette
- documented update_changelog.py script
- updated changelog
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-26   --   v0.1.7</p>
            <p>========================</p>
            </b>
        </div>

- Added automatic changelog updates on succesfull pr-request. Automatic changelog updates add commit messages of all commits (some filtering applies) between the LAST_COMMIT_HASH defined in scripts/update_changelog.py and the current commit.
- Added show_bar_values functionality
- restructuring src code into separate style and functions files
- create example script for mighty python session
- Added CHANGELOG
- fixed a legend issue with labels on barplots
- refactored palettes to be matplotlib colormaps. Added gradients for heatmaps
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-25   --   v0.1.6</p>
            <p>========================</p>
            </b>
        </div>

- updated workflows
- removed scipy dependency by copying nnls code into local file
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-24   --   v0.1.5</p>
            <p>========================</p>
            </b>
        </div>

- updated workflow caching to take into account python version
- Added python 3.10 support
- updated dependencies to include scipy
- updated workflows to auto-commit code reformatted in the linting job
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-24   --   v0.1.4</p>
            <p>========================</p>
            </b>
        </div>

- cleaned up poetry environment
- updated palette default to represent colors in correct order
- fixed typo in chart title
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-17   --   v0.1.3</p>
            <p>========================</p>
            </b>
        </div>

- combined example images into single image for README
- gitignore update
- fix issue with multi line legends in lineplot
- fix issue with line legends at logarithmic scale
- set horizontal distance of linelegend to be based on xrange and not on x-axis
- refactored testing to be more in line with code structure
- merging linelegend with legend to have a single legend call
- change green tone of title and axis, moved green_bright more in the back of the line
- added .flake8 + black in pipeline
- adjusted color palette to be more in line with branding
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-15   --   v0.1.2</p>
            <p>========================</p>
            </b>
        </div>

- Initial release
- Created workflows to maintain the project
- Added default colors
- Added legend and legend_line functionalities
- Added ylabel functionality
- Added dataroots style usable globally or with context manager
- Added CodeCoverage, PyPI badge, Python Badge and Maintainer badge to README
- Added README with install and usage explanation