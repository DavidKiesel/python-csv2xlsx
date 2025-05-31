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
version = '1.0.0.dev'

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

    # Sets setup.py variable description.
    project.summary = \
        'Read a CSV file and write an XLSX file with optional formatting.' 

    # Sets setup.py variable long_description.
    project.description = """
    Read a CSV file and write an XLSX file with optional formatting.
    """

    # Sets setup.py variable author and author_email.
    project.authors = \
        (
            Author(
                'David Harris Kiesel',
                'david.sw@suddenthought.net'
            ),
        )

    # Sets setup.py variable maintainer and maintainer_email.
    project.maintainers = \
        (
            Author(
                'David Harris Kiesel',
                'david.sw@suddenthought.net'
            ),
        )

    # Sets setup.py variable license.
    # See:
    # * https://choosealicense.com/
    # * https://spdx.org/licenses/
    project.license = 'MIT'

    # Sets setup.py variable url.
    project.url = 'https://github.com/DavidKiesel/python-csv2xlsx'

    # Sets setup.py variable project_urls.
    project.urls = \
        {
            'Homepage': 'https://github.com/DavidKiesel/python-csv2xlsx',
        }

    # Sets setup.py variable python_requires.
    project.requires_python = '>=3.8'

@init
def set_properties(
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
            'License :: OSI Approved :: MIT License',
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

    # Sets twine option --repository argument.
    # To upload to pypi, this setting can be overridden with pyb argument
    # `-P 'distutils_upload_repository_key=pypi'`.
    project.set_property(
        'distutils_upload_repository_key',
        'testpypi'
    )
