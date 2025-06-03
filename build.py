#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2025 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

##############################################################################
# build.py documentation:
#
# PyBuilder usage documentation at https://pybuilder.io/documentation/manual.

##############################################################################
# Imports.

from pybuilder.core import (
    Author,
    init,
    use_plugin,
)

##############################################################################
# Plugins.
#
# https://pybuilder.io/documentation/plugins

use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')
use_plugin('python.unittest')
#use_plugin('python.integrationtest')
use_plugin('python.coverage')
use_plugin('python.distutils')
# Sphinx plugin created API documentation for `python.dhk.csv2xlsx`
# instead of `dhk.csv2xlsx` so not using it.
# https://www.sphinx-doc.org/en/master/
# use_plugin('python.sphinx')

##############################################################################
# Project attributes set as global variables.
#
# Note that, while the PyBuilder documentation indicates that project
# attributes can be set as global variables or as `project` instance attributes
# within an initializer function, the naming of the Python package distribution
# files does not work correctly by default as of PyBuilder version 0.13.15
# unless `name` and `version` are set as global variables.  See
# https://github.com/pybuilder/pybuilder/issues/646.

# Sets setup.py `name` variable.
name = 'dhk.csv2xlsx'

# Sets setup.py `version` variable.
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#choosing-a-versioning-scheme
# https://www.python.org/dev/peps/pep-0440/
version = '1.0.1'

##############################################################################
# Functions.

@init
def initialize(project):
    """
    Initialize the project.

    Project attributes can be set as global variables or as attributes of the
    `project` object.
    """

    # A `str` or `list[str]`.
    project.default_task = \
        (
            'clean',
            'analyze',
            'publish',
        )

    # Sets `setup.py` variable `description`.
    project.summary = \
        'Read a CSV file and write an XLSX file with optional formatting.'

    # Sets `setup.py` variable `long_description`.
    # Not needed because using README file through distutils plugin.
    # project.description = ''

    # Sets `setup.py` variables `author` and `author_email`.
    project.authors = \
        (
            Author(
                'David Harris Kiesel',
                'david.sw@suddenthought.net'
            ),
        )

    # Sets `setup.py` variables `maintainer` and `maintainer_email`.
    project.maintainers = \
        (
            Author(
                'David Harris Kiesel',
                'david.sw@suddenthought.net'
            ),
        )

    # Sets `setup.py` variable `license`.
    # See:
    # * https://choosealicense.com/
    # * https://spdx.org/licenses/
    project.license = 'MIT'

    # Sets `setup.py` variable `url`.
    project.url = 'https://github.com/DavidKiesel/python-csv2xlsx'

    # Sets `setup.py` variable `project_urls`.
    project.urls = \
        {
            'Homepage': 'https://github.com/DavidKiesel/python-csv2xlsx',
        }

    # Sets `setup.py` variable `python_requires`.
    project.requires_python = '>=3.8'

@init
def set_properties_001(
    project
):
    ##########################################################################
    # install_dependencies plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    project.depends_on_requirements(
        'requirements.txt'
    )

    project.depends_on_requirements(
        'requirements-dev.txt'
    )

    ##########################################################################
    # flake8 plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    project.set_property(
        'flake8_break_build',
        True
    )

    project.set_property(
        'flake8_include_test_sources',
        True
    )

    # E123 closing bracket does not match indentation of opening bracket's line
    # E501 line too long (N > 79 characters)
    # W503 line break before binary operator
    # W504 line break after binary operator
    project.set_property(
        'flake8_ignore',
        'E123,E501,W503,W504'
    )

    ##########################################################################
    # coverage plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    project.set_property(
        'coverage_break_build',
        False
    )

    ##########################################################################
    # distutils plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    # Sets setup.py variable classifiers.
    # https://pypi.org/classifiers/
    project.set_property(
        'distutils_classifiers',
        (
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
        )
    )

    # If `distutils_readme_description` and `distutils_description_overwrite`
    # are both True, then contents of the README file (e.g., `README.md`) will
    # be used to set the PyPI page's `Project description` instead of the value
    # of the project attribute `description`.
    #
    # Note that the README file can be set by project property
    # `distutils_readme_file` but defaults to `README.md`.
    project.set_property(
        'distutils_readme_description',
        True
    )

    project.set_property(
        'distutils_description_overwrite',
        True
    )

    # Sets twine option --repository argument.
    project.set_property(
        'distutils_upload_repository_key',
        'testpypi'
    )

@init(
    environments='pypi'
)
def set_properties_002(
    project
):
    ##########################################################################
    # distutils plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    # Sets twine option --repository argument.
    project.set_property(
        'distutils_upload_repository_key',
        'pypi'
    )
