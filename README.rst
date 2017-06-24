========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-check-pypi-name/badge/?style=flat
    :target: https://readthedocs.org/projects/python-check-pypi-name
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/python-check-pypi-name.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/python-check-pypi-name

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/python-check-pypi-name?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/python-check-pypi-name

.. |requires| image:: https://requires.io/github/techdragon/python-check-pypi-name/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/python-check-pypi-name/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/techdragon/python-check-pypi-name/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/techdragon/python-check-pypi-name

.. |codecov| image:: https://codecov.io/github/techdragon/python-check-pypi-name/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/python-check-pypi-name

.. |version| image:: https://img.shields.io/pypi/v/check-pypi-name.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/check-pypi-name

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/python-check-pypi-name/v0.2.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/python-check-pypi-name/compare/v0.2.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/check-pypi-name.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/check-pypi-name

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/check-pypi-name.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/check-pypi-name

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/check-pypi-name.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/check-pypi-name


.. end-badges

Check if a package name is registered with PyPI

* Free software: BSD license

Installation
============

::

    pip install check-pypi-name

Documentation
=============

https://python-check-pypi-name.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
