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

- merging workflows back together
- splitting gh actions into multiple files
- move codecov to separate yml file
- update utils unused code + push.yml
- updated push.yml
- limited poetry file to python between 3.8 and 3.10
- remove python 3.11 support since it is not yet supported by the usd GH action
- added python 3.11 support
- copied scipy optimize nnls code to remove dependency
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-24   --   v0.1.5</p>
            <p>========================</p>
            </b>
        </div>

- updated caching to take into account python version
- Adding back python 3.10 support
- updated dependencies to take into account scipy optimize usage
- change in main.py to test auto commit
- updated push.yml to autocommit changes made by black reformatting
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-24   --   v0.1.4</p>
            <p>========================</p>
            </b>
        </div>

- update push workflow
- update push workflow
- cleaned up poetry environment
- Merge branch 'main' into v0.1.4
- updated palette default to represent colors in correct order
- fix typo in chart title
- Merge branch 'main' into v0.1.4
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-11-17   --   v0.1.3</p>
            <p>========================</p>
            </b>
        </div>

- added dir for tests
- combined example images
- gitignore update
- solved multi line legends in lineplot
- implemented log line legend
- fixed horizontal distance of linelegend to be based on xrange and not on xax
- refactored testing to be in line with main.py structure
- split testing and image plotting
- refactoring main.py
- merging linelegend with legend
- change green tone of title and axis, moved green_bright more in the back of the line
- regenerated images
- adapted push.yml
- temp revert to pushing main = testing + linting
- added .flake8 + black in pipeline + adjusted palette to be more in line with branding
- Merge pull request #3 from datarootsio/ylabel
- added palette
- adding more colors
- added caching again
- update pr
- Merge branch 'ylabel' into main
- updated pr and push actions"
- Merge pull request #2 from datarootsio/ylabel
- removed python 3.10 support due to latest scipy version not supporting python 3.10
- poetry install
- update push.yml
- updated python versions
- PyPI badge
- updated workflows
- Merge pull request #1 from datarootsio/ylabel
- updated pr.yml
- updated push.yml
- added ylabel functionality
- version update
- update push.yml
- PR workflow name change
- added linting to push.yml and added pr.yml
- added lineplot legend
- removed requirements.txt since poetry install works fine
- updated gitignore
- updated legend + ci.yml
- added back lightgray to colors
- added sparkly stones barplot, updated colors
- added source above style in __main__.py
- removed caching
- testing caching
- testing caching
- reset caching
- removed caching
- trailing whitespace
- changed pytest command
- fixed caching... again
- forgot to add test commands
- fixed caching
- added caching to ci.yml
- added requirements.txt file because poetry takes hella long
- fixed versions in pyproject.toml
- poetry install in virtual env
- updated ci.yml
- updated poetry.lock file
- updated ci.yml
- updated ci.yml
- update ci.yml
- Updated ci.yml and the README
- Committed initial code + CI + Testing
- added README images
- first commit
