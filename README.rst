substancek_cms_theme
====================

This is an experimental plugin based on ``Kotti``.

It provides:

* a clone of the Kotti's default theme

* integration by default with the Yeoman toolchain (SASS, html minification, image optimization, etc)

* public website decoupled from the private content administration area

|build status|_
|code coverage|_

.. |build status| image:: https://secure.travis-ci.org/substancek/substancek_cms_theme.png?branch=master
.. _build status: http://travis-ci.org/substancek/substancek_cms_theme
.. |code coverage| image:: http://codecov.io/github/substancek/substancek_cms_theme/coverage.svg?branch=master
.. _code coverage: http://codecov.io/github/substancek/substancek_cms_theme?branch=master

Requirements
------------

* Python 2.7

* nodejs >= 0.12

* npm (latest)

* gulp-cli

* bower

How to install substancek_cms_theme
-----------------------------

It is simple (**to be fixed**)::

    $ make install-prerequisites     # performs some apt-get install, you need sudo
    $ make install-dev
    $ make run-dev

Visit:

* http://localhost:5000/ (public website)
* http://localhost:5000/cms (backend with admin / qwerty authentication)
