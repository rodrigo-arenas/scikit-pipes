.. -*- mode: rst -*-

|Tests|_ |Codecov|_ |PythonVersion|_ |PyPi|_ |Docs|_

.. |Tests| image:: https://github.com/rodrigo-arenas/scikit-pipes/actions/workflows/ci-tests.yml/badge.svg?branch=master
.. _Tests: https://github.com/rodrigo-arenas/scikit-pipes/actions/workflows/ci-tests.yml

.. |Codecov| image:: https://codecov.io/gh/rodrigo-arenas/scikit-pipes/branch/master/graphs/badge.svg?branch=master&service=github
.. _Codecov: https://codecov.io/github/rodrigo-arenas/scikit-pipes?branch=master

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue
.. _PythonVersion : https://www.python.org/downloads/

.. |PyPi| image:: https://badge.fury.io/py/scikit-pipes.svg
.. _PyPi: https://badge.fury.io/py/scikit-pipes

.. |Docs| image:: https://readthedocs.org/projects/scikit-pipes/badge/?version=latest
.. _Docs: https://scikit-pipes.readthedocs.io/en/latest/?badge=latest

.. |Contributors| image:: https://contributors-img.web.app/image?repo=rodrigo-arenas/scikit-pipes
.. _Contributors: https://github.com/rodrigo-arenas/scikit-pipes/graphs/contributors


.. image:: https://github.com/rodrigo-arenas/scikit-pipes/blob/master/docs/images/logo16.png?raw=true
   :width: 100

Scikit-Pipes
############

Scikit-Learn useful pre-defined Pipelines Hub.

This package is still at an experimental stage.

Usage:
######

Install scikit-pipes

It's advised to install scikit-pipes using a virtual env, inside the env use::

   pip install scikit-pipes

Example: Simple Preprocessing
#############################

.. code-block:: python

    import pandas as pd
    import numpy as np
    from skpipes.pipeline import SkPipeline

    data = [{"x1": 1, "x2": 400, "x3": np.nan},
            {"x1": 4.8, "x2": 250, "x3": 50},
            {"x1": 3, "x2": 140, "x3": 43},
            {"x1": 1.4, "x2": 357, "x3": 75},
            {"x1": 2.4, "x2": np.nan, "x3": 42},
            {"x1": 4, "x2": 287, "x3": 21}]

    df = pd.DataFrame(data)

    pipe = SkPipeline(name='imputer_median-minmax',
                      data_type="numerical")
    pipe.steps
    str(pipe)

    pipe.fit(df)
    pipe.transform(df)
    pipe.fit_transform(df)


Changelog
#########

See the `changelog <https://scikit-pipes.readthedocs.io/en/latest/release_notes.html>`__
for notes on the changes of Sklearn-pipes

Important links
###############

- Official source code repo: https://github.com/rodrigo-arenas/scikit-pipes/
- Download releases: https://pypi.org/project/scikit-pipes/
- Issue tracker: https://github.com/rodrigo-arenas/scikit-pipes/issues
- Stable documentation: https://scikit-pipes.readthedocs.io/en/stable/

Source code
###########

You can check the latest development version with the command::

   git clone https://github.com/rodrigo-arenas/scikit-pipes.git

Install the development dependencies::

  pip install -r dev-requirements.txt

Check the latest in-development documentation: https://scikit-pipes.readthedocs.io/en/latest/

Testing
#######

After installation, you can launch the test suite from outside the source directory::

   pytest skpipes
