pytest plugin to implement a ``--failed`` option

Warning
=======

This project is no longer maintained.

If you are using ``pytest >= 2.8`` you don't need to install anything,
since the functionality has been added to ``pytest core``

If you are using ``pytest <= 2.7`` you should use
use `pytest-cache <https://pypi.python.org/pypi/pytest-cache>`_ instead.

* It provides the same feature with ``--lf`` instead of ``--failed``
  (which is shorter)

* It's developed by the original author of ``pytest`` (Holger Krekel)

* It has more features

* It does not use ``pickle`` for storing data so it's safe to use
  across different versions of Python

The only downside is that ``pytest-cache`` depends on ``execnet``,
whereas ``pytest-runfailed`` is standalone.


Usage
=====

Just run ::

  py.test --failed


You'll need to run the full suite once before the option
``--failed`` can work.

The failing tests ids are stored into a ``.pytest`` directory,
just remove it if you experience issues.
