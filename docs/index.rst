Facio Documentation
===================

Facio: /ˈfa.ki.oː/ - Latin, meaning to make, do, act, perform, cause, bring about.

What is it?
-----------

If you work on quick turn around projects either at work or in your free time you might end up doing a lot of boiler plate cruft for your projects over and over, creating the same basic template. You might copy and paste this around, it might fall out of date, you might make improvements in a project but forget about them for the next.

``Facio`` gives you the ability to create a standard template (or templates) for your projects so you can bootstrap in one single command.

Originally developed with `Django`_ in mind you can use ``Facio`` for any type of project.

Status
------

**Current Version:** 1.1.1

Tests are run using `Travis CI`_.

* **Master Branch (Stable):** |travis_master|

* **Develop Branch (Active Development):** |travis_develop|

Features
--------

* Custom Templates
* Git support for remote templates
* Multiple templates
* `Jinja2`_ Templates
* Python virtualenv creation
* Configuration using ``.facio.cfg``

Topics
------

.. toctree::
    :maxdepth: 3

    installing
    usage
    templates
    developing
    changelog

License
-------

See LICENSE file in the `Git Repository`_.

Authors
-------

See LICENSE file in the `Git Repository`_.

Special Thanks
--------------

To the Tech Team at `Poke London`_ and the awesome `Jinja2`_.

And thanks to Jack for helping me name it (and pointing out grammatical errors). <3.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. Links
.. _Django: https://www.djangoproject.com/
.. _Travis CI: https://travis-ci.org/krak3n/Facio
.. _Jinja2: http://jinja.pocoo.org/docs/
.. _Git Repository: https://github.com/krak3n/facio
.. _Poke London: http://pokelondon.com

.. Images
.. |travis_master| image:: https://travis-ci.org/krak3n/Facio.png?branch=master
    :height: 18px
.. |travis_develop| image:: https://travis-ci.org/krak3n/Facio.png?branch=develop
    :height: 18px
