substancek_cms_theme
====================

|build status|_
|code coverage|_

.. |build status| image:: https://secure.travis-ci.org/substancek/substancek_cms_theme.png?branch=master
.. _build status: http://travis-ci.org/substancek/substancek_cms_theme
.. |code coverage| image:: http://codecov.io/github/substancek/substancek_cms_theme/coverage.svg?branch=master
.. _code coverage: http://codecov.io/github/substancek/substancek_cms_theme?branch=master

``substancek_cms_theme`` is a http://kotti.pylonsproject.org based project that:

* provides a clone of the Kotti's default theme

* shows how to integrate and distribute a Python package integrated with a Yeoman setup (http://yeoman.io)

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

Once installed ``Kotti`` and the other requirements clone this package and type::

    $ virtualenv --no-site-packages python
    $ source python/bin/activate
    $ pip install -r requirements.txt
    $ python setup.py develop
    $ python setup.py build_all
    $ pserve development.ini

and visit:

* http://localhost:5000/ (public website)
* http://localhost:5000/admin (backend with admin / qwerty authentication)
