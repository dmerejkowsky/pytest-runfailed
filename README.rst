pytest plugin to implement a ``--failed`` option

Usage
=====

Just run ::

  py.test --failed


You'll need to run the full suite once before the option
``--failed`` can work.

The failing tests ids are stored into a ``.pytest`` directory,
just remove it if you experience issues.
