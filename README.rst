|Icon| |title|_
===============

.. |title| replace:: scikit-zhangt20-lvl5
.. _title: https://TingwenZhang.github.io/scikit-zhangt20-lvl5

.. |Icon| image:: https://avatars.githubusercontent.com/TingwenZhang
        :target: https://TingwenZhang.github.io/scikit-zhangt20-lvl5
        :height: 100px

|PyPi| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/TingwenZhang/scikit-zhangt20-lvl5/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/TingwenZhang/scikit-zhangt20-lvl5/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/TingwenZhang/scikit-zhangt20-lvl5/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/TingwenZhang/scikit-zhangt20-lvl5

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/scikit-zhangt20-lvl5
        :target: https://anaconda.org/conda-forge/scikit-zhangt20-lvl5

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPi| image:: https://img.shields.io/pypi/v/scikit-zhangt20-lvl5
        :target: https://pypi.org/project/scikit-zhangt20-lvl5/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/scikit-zhangt20-lvl5
        :target: https://pypi.org/project/scikit-zhangt20-lvl5/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/TingwenZhang/scikit-zhangt20-lvl5/issues

Level 5 for scikit-package

* LONGER DESCRIPTION HERE

For more information about the scikit-zhangt20-lvl5 library, please consult our `online documentation <https://TingwenZhang.github.io/scikit-zhangt20-lvl5>`_.

Citation
--------

If you use scikit-zhangt20-lvl5 in a scientific publication, we would like you to cite this package as

        scikit-zhangt20-lvl5 Package, https://github.com/TingwenZhang/scikit-zhangt20-lvl5

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``scikit-zhangt20-lvl5_env`` ::

        conda create -n scikit-zhangt20-lvl5_env scikit-zhangt20-lvl5
        conda activate scikit-zhangt20-lvl5_env

To confirm that the installation was successful, type ::

        python -c "import scikit_zhangt20_lvl5; print(scikit_zhangt20_lvl5.__version__)"

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``scikit-zhangt20-lvl5_env`` environment, type ::

        pip install scikit-zhangt20-lvl5

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/TingwenZhang/scikit-zhangt20-lvl5/>`_. Once installed, ``cd`` into your ``scikit-zhangt20-lvl5`` directory
and run the following ::

        pip install .

Getting Started
---------------

You may consult our `online documentation <https://TingwenZhang.github.io/scikit-zhangt20-lvl5>`_ for tutorials and API references.

Support and Contribute
----------------------

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/TingwenZhang/scikit-zhangt20-lvl5/issues>`_ and/or `submit a fix as a PR <https://github.com/TingwenZhang/scikit-zhangt20-lvl5/pulls>`_.

Feel free to fork the project and contribute. To install scikit-zhangt20-lvl5
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contributing, please read our `Code of Conduct <https://github.com/TingwenZhang/scikit-zhangt20-lvl5/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on scikit-zhangt20-lvl5 please visit the project `web-page <https://TingwenZhang.github.io/>`_ or email Tingwen Zhang at zhangt20@rpi.edu.

Acknowledgements
----------------

``scikit-zhangt20-lvl5`` is built and maintained with `scikit-package <https://billingegroup.github.io/scikit-package/>`_.
