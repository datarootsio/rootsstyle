# Contributing

We are always looking for contributions! You can find below some relevant information and
standards for `rootsstyle`.

## Setup ⚙️

After cloning the [repo](https://github.com/datarootsio/rootsstyle/), make sure to set up
the environment.

### Poetry 📜

We use [Poetry](https://python-poetry.org/) for both managing environments and packaging.
That means you need to install poetry but from there you can use the tool to create the
environment.

```bash
pip install poetry==1.1.12
poetry install  # installs prod and dev dependencies
```

#### Usage

Remember that to use the environment you can use the `poetry run <COMMAND>` command or
initialize the shell with `poetry shell`. For example, if you want to create the
coverage report you could run

```bash
poetry run pytest --cov=rootsstyle tests/
```

or alternatively

```bash
poetry shell
pytest --cov=rootsstyle tests/
```

## Development 🛠

We welcome new features, bugfixes or enhancements (whether on code or docs). There are a
few standards we adhere to, that are required for new features.

### Type hints

We use type hints! There are a couple of reasons for using type hints, mainly:

1. Better code coverage (avoid errors during runtime)
2. Improve code understanding

### Linting

In regards to code quality, we use a couple of linting tools to maintain the same "style"
and uphold to the same standards. For that, we use:

1. [Black](https://black.readthedocs.io/en/stable/) for code formatting
2. [isort](https://pycqa.github.io/isort/) for imports
3. [Flake8](https://pycqa.github.io/isort/) for style enforcement

## Docs 📚

As for documentation, the `rootsstyle` documentation "lives" both on the code itself and
supporting documentation (markdown) files.

### Code
Code docs include annotating type hints as well as function docstrings.

## Tests 🗳

We use unit tests to ensure that our package works as expected. We use
[`pytest`](https://docs.pytest.org/en/6.2.x/) for testing and
[`Pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) for checking how much of
the code is covered in our tests.

The tests should mimic the package directory structure. The tests are also written to
serve as an example of how to use the classes and methods and expected outputs.


## Publishing

Publishing is automatically done via [Github Actions](https://github.com/features/actions)
to PiPy. After published, a new tag and release are created. The Changelog is also automatically updated based on your commits.

## Contributors 👨‍💻👩‍💻

`rootsstyle` was created by [Yannou Ravoet](https://github.com/YannouRavoet), and is
maintained by [dataroots](https://github.com/datarootsio).

### Acknowledgements

Special thanks to:

[Bart](https://github.com/Bart6114) and [Dorian](https://github.com/devdnhee) for feedback and support.