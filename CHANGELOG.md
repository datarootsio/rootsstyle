## [0.3.0](https://github.com/datarootsio/rootsstyle/compare/v0.2.4...v0.3.0) (2021-12-06)
  
  
  ### Features
  
  * **workflow_rework:** automated tagging, releasing, publishing, updating changelog and updating visualizations ([610ca58](https://github.com/datarootsio/rootsstyle/commit/610ca58b4ef98faee6d253e0192b20c1db838801))
  
  
  ### Bug Fixes
  
  * **workflow_linting:** disabled workflow if changes are made by the linting step. ([48da103](https://github.com/datarootsio/rootsstyle/commit/48da103587b9ddaecbafc1bea7f75cee98629865))
  * **workflow_push:** added step to cancel previous workflows so that linting changes stop previous workflows ([821c012](https://github.com/datarootsio/rootsstyle/commit/821c012e44d2b0f73d58cb32be6ca7f4d15a1284))
  * **workflow_push:** moved update changelog to before publishing. This should not matter much, but is more intuitively correct ([7468ae5](https://github.com/datarootsio/rootsstyle/commit/7468ae5d5c4247683533c452b139cfe3ab198156))
  
  
  ### Tests
  
  * **show_bar_values:** added tests for show_bar_values ([46b3e5b](https://github.com/datarootsio/rootsstyle/commit/46b3e5b996df259381b1fbce551b992671afc4fd))
  * **show_bar_values:** fixed syntax error in test ([6cdd139](https://github.com/datarootsio/rootsstyle/commit/6cdd1392020273325bf88b3bd69cabb41dffd549))
  * **workflow_push:** testing cancellation on automatted commit after linting ([f0e3dd6](https://github.com/datarootsio/rootsstyle/commit/f0e3dd6b9e16d3ae79f577712b8af38a433c7abf))
  
  
  ### Styles
  
  * **black:** Automated reformatting done by black ([abec874](https://github.com/datarootsio/rootsstyle/commit/abec87446b185fbab117b8127c6a0679e74fd856))
  * **black:** Automated reformatting done by black ([b36c48d](https://github.com/datarootsio/rootsstyle/commit/b36c48ddbf9b9477f98e6eb6e2b8d466fc0ac2b3))
  * **black:** Automated reformatting done by black ([1a7b891](https://github.com/datarootsio/rootsstyle/commit/1a7b891751953b0a278cbfaac719b630fd379ad3))
  * **black:** Automated reformatting done by black ([9637e15](https://github.com/datarootsio/rootsstyle/commit/9637e159b24c20afacb69e0c4462e19a4332ad2f))
  * **black:** Automated reformatting done by black ([1e0d9dc](https://github.com/datarootsio/rootsstyle/commit/1e0d9dcb2d83603612fc87559fdb4e1d6bb7ab4a))
  * **black:** Automated reformatting done by black ([d6f14c0](https://github.com/datarootsio/rootsstyle/commit/d6f14c0f9f1a20e23ad7c5394f003964136fa4f5))
  * **README:** alignment update ([d745758](https://github.com/datarootsio/rootsstyle/commit/d745758738268e89f514bdc03f60f0697e9173d2))
  
  
  ### Code Refactoring
  
  * **gitignore:** updated gitignore ([658fdd2](https://github.com/datarootsio/rootsstyle/commit/658fdd2e500e70f12edbe9381119f1836f1b1301))
  * **linting:** refactored linting workflow to use predefined actions ([4ba637e](https://github.com/datarootsio/rootsstyle/commit/4ba637e3bf8b1c02622e970f77436243127e754a))
  * **test_plots:** made output dir an argument so that local testing does not create images ([2198d74](https://github.com/datarootsio/rootsstyle/commit/2198d74f5190244d62f9608b22ed4e9757dff5a6))
  * **workflows:** removed backup directory ([1a8e8f9](https://github.com/datarootsio/rootsstyle/commit/1a8e8f9864c0ba7a10c7a5d4dc8e9cd12e6476d5))
  
  
  ### Documentation
  
  * **CHANGELOG:** Automated commit of CHANGELOG.md update ([fb13378](https://github.com/datarootsio/rootsstyle/commit/fb133784c63407a7e352d0af3e0b5f74c3b28b36))
  * **README:** added versioning section ([067050c](https://github.com/datarootsio/rootsstyle/commit/067050c6da28b8d82bb4372b142e3807cb0a7f4d))
  * **README:** alignment of images in tables ([bff5b5f](https://github.com/datarootsio/rootsstyle/commit/bff5b5f7ad821f05c150296ebff30f41cbb6850f))
  * **README:** alignment update ([6351b85](https://github.com/datarootsio/rootsstyle/commit/6351b85b036b3315637afa3ad9c90d49dbb6b61f))
  * **README:** remove ROADMAP section that was done ([544c122](https://github.com/datarootsio/rootsstyle/commit/544c122707d48efd3900700a9696840c1b44472b))
  * **README:** update image links for examples in README ([1944ff1](https://github.com/datarootsio/rootsstyle/commit/1944ff1da8395c66e7556c9ad6794b882ad5346c))
  * **README:** updated versioning section ([2bc2c0a](https://github.com/datarootsio/rootsstyle/commit/2bc2c0a800bf0efd2427ed4dbcf50ba9a946535c))
  * **visualizations:** Automated update of visualizations used in README ([0e92004](https://github.com/datarootsio/rootsstyle/commit/0e920046267f350af146532c9529725424fa7185))
  * **visualizations:** Automated update of visualizations used in README ([e290b7c](https://github.com/datarootsio/rootsstyle/commit/e290b7c77e7b7995802f0929ce3c3a455ea6a002))
  * **visualizations:** Automated update of visualizations used in README ([87ebaae](https://github.com/datarootsio/rootsstyle/commit/87ebaaec81d81329a8aac7e1577a5435796a5969))
  * **visualizations:** Automated update of visualizations used in README ([877d801](https://github.com/datarootsio/rootsstyle/commit/877d801e39f3a8bfaa364e1398c1ddcaa6176169))
  * **visualizations:** Automated update of visualizations used in README ([8b310bc](https://github.com/datarootsio/rootsstyle/commit/8b310bc9bbdd0a2cc3e3b92a290be410a2425e05))
  * **visualizations:** Automated update of visualizations used in README ([113ee63](https://github.com/datarootsio/rootsstyle/commit/113ee63be71527cb12ac82db25e58b39aa43e874))
  
  


<div align=center>
            <b>
            <p>========================</p>
            <p>2021-12-03   --   v0.1.9</p>
            <p>========================</p>
            </b>
        </div>

- added python 3.7.1 support for Google Colab
- Set theme jekyll-theme-cayman
- moved examples.ipynb to examples directory
- fixed .gitignore to include test data
- fixed import in rootsstyle/__init__.py
- moved flake8 and black configurations to .flake8 and pyproject.toml
- renamed main files
- added example to README
- removed scripts from pyproject.toml since this is unnecessary
<div align=center>
            <b>
            <p>========================</p>
            <p>2021-12-01   --   v0.1.8</p>
            <p>========================</p>
            </b>
        </div>
        
- fixed branch misdirect in changelog GH actions
- set default text color to textgray
- added public colorlist as rootsstyle.colors
- added example of data point label in scatterplot
- added example of ytick rotation in heatmaps
- updated dataroots-green-to-blue palette
- documented update_changelog.py script
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
