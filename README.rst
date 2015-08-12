substancek_cms_theme
====================

|build status|_
|code coverage|_

.. |build status| image:: https://secure.travis-ci.org/substancek/substancek_cms_theme.png?branch=master
.. _build status: http://travis-ci.org/substancek/substancek_cms_theme
.. |code coverage| image:: http://codecov.io/github/substancek/substancek_cms_theme/coverage.svg?branch=master
.. _code coverage: http://codecov.io/github/substancek/substancek_cms_theme?branch=master

``substancek_cms_theme`` is a layer upon the ``Kotti`` framework that provides:

* a clone of the Kotti's default theme

* integration by default with the Yeoman toolchain (SASS, html minification, image optimization, etc)

* public website decoupled from the private content administration area

Requirements
------------

* Python 2.7

* Kotti

* nodejs >= 0.12

* npm (latest)

* gulp-cli

* bower

Installation
------------

Once installed Kotti and the other requirements clone this package and type::

    $ python setup.py develop
    $ python setup.py build_all
    $ pserve development.ini

and visit:

* http://localhost:5000/ (public website)
* http://localhost:5000/cms (backend with admin / qwerty authentication)
