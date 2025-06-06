dhk.csv2xlsx
============

[![GitHub](https://img.shields.io/badge/github-python--csv2xlsx-blue?logo=github)](https://github.com/DavidKiesel/python-csv2xlsx)

[![Latest Version](https://img.shields.io/pypi/v/dhk.csv2xlsx?logo=pypi)](https://pypi.org/project/dhk.csv2xlsx/)
[![Python Versions](https://img.shields.io/pypi/pyversions/dhk.csv2xlsx?logo=pypi)](https://pypi.org/project/dhk.csv2xlsx/)

[![Downloads Per Day](https://img.shields.io/pypi/dd/dhk.csv2xlsx?logo=pypi)](https://pypi.org/project/dhk.csv2xlsx/)
[![Downloads Per Week](https://img.shields.io/pypi/dw/dhk.csv2xlsx?logo=pypi)](https://pypi.org/project/dhk.csv2xlsx/)
[![Downloads Per Month](https://img.shields.io/pypi/dm/dhk.csv2xlsx?logo=pypi)](https://pypi.org/project/dhk.csv2xlsx/)

# Introduction

`dhk.csv2xlsx` is a Python command-line tool for reading a CSV file and writing an XLSX file with optional formatting.
It leverages the Python standard library [`csv`](https://docs.python.org/3/library/csv.html) module and the [`XlsxWriter`](https://pypi.org/project/XlsxWriter/) package.

# Simple Installation

A pedestrian command for installing the package is given below.
Alternatively, for a more rewarding installation exercise, see section [Recommended Installation](#recommended-installation).

```bash
pip install dhk.csv2xlsx
```

# Usage

```console
$ csv2xlsx --help
usage: csv2xlsx [-h] [--settings-file SETTINGS_FILE] [--verbose] [--force]
                [--output OUTPUT_FILE]
                CSV_FILE

Read a CSV file and write an XLSX file.

positional arguments:
  CSV_FILE              CSV file

options:
  -h, --help            show this help message and exit
  --settings-file, -s SETTINGS_FILE
                        settings file; default: None
  --verbose, -v         verbose
  --force, -f           force; suppress prompts
  --output, -o OUTPUT_FILE
                        output file; default: CSV_FILE - .csv + .xlsx

Examples:

    csv2xlsx \
        CSV_FILE

    csv2xlsx \
        --settings-file SETTINGS_FILE \
        CSV_FILE

    csv2xlsx \
        --settings-file SETTINGS_FILE \
        --output OUTPUT \
        CSV_FILE
```

# Recommended Installation

[`pyenv`](https://github.com/pyenv/pyenv) is a tool for installing multiple Python environments and controlling which one is in effect in the current shell.

[`pipx`](https://github.com/pipxproject/pipx) is a tool for installing and running Python applications in isolated environments.

Assuming these have been installed correctly...

## Install Python Under `pyenv`

The version of Python under which this package was last developed and tested is stored in [`.python-version`](https://raw.githubusercontent.com/DavidKiesel/python-csv2xlsx/refs/heads/main/.python-version).

To capture this Python version to a shell variable, execute the commands below.
`PYTHON_VERSION` should be set to something like `3.13.3`.

```bash
PYTHON_VERSION="$(
    wget \
        -O - \
        https://raw.githubusercontent.com/DavidKiesel/python-csv2xlsx/refs/heads/main/.python-version
)"

echo "$PYTHON_VERSION"
```

To determine if the `.python-version` version of Python has already been installed under `pyenv`, execute the command below.
If it has not been installed, then a warning message will be displayed.

```bash
PYENV_VERSION="$PYTHON_VERSION" \
python --version
```

If it has already been installed, then proceed to section [Install Package Using `pipx`](#install-package-using-pipx).

Otherwise, to install the given version of Python under `pyenv`, execute the command below.

```bash
pyenv install "$PYTHON_VERSION"
```

If the install was successful, then proceed to section [Install Package Using `pipx`](#install-package-using-pipx).

If instead there is a warning that the definition was not found, then you will need to upgrade `pyenv`.

If `pyenv` was installed through a package manager, then consider upgrading it through that package manager.
For example, if `pyenv` was installed through `brew`, then execute the commands below.

```bash
brew update

brew upgrade pyenv
```

Alternatively, you could attempt to upgrade `pyenv` through the command below.

```bash
pyenv update
```

Once `pyenv` has been upgraded, to install the given version of Python under `pyenv`, execute the command below.

```bash
pyenv install "$PYTHON_VERSION"
```

## Install Package Using `pipx`

Only proceed from here if the instructions in section [Install Python Under `pyenv`](#install-python-under-pyenv) have been completed successfully.

At this point, shell variable `PYTHON_VERSION` should already contain the appropriate Python version.
If not, execute the commands below.

```bash
PYTHON_VERSION="$(
    wget \
        -O - \
        https://raw.githubusercontent.com/DavidKiesel/python-csv2xlsx/refs/heads/main/.python-version
)"

echo "$PYTHON_VERSION"
```

To install the package hosted at PyPI using `pipx`, execute the command below.

```bash
pipx \
    install \
    --python "$(PYENV_VERSION="$PYTHON_VERSION" pyenv which python3)" \
    dhk.csv2xlsx
```
