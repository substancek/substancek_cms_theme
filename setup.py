import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'Kotti>=1.0.0',
    'Paste',
    'kotti_backend',
    'pyramid_html_minifier',
    'build_commands',
    ]

test_requirements = [
    'Kotti[testing]',
    'WebTest',
    'mock',
    'py>=1.4.29',
    'pyquery',
    'pytest>=3.0.0',
    'pytest-cov',
    'pytest-pep8!=1.0.3',
    'pytest-travis-fold',
    'pytest-virtualenv',
    'pytest-xdist',
    'tox',
    'virtualenv',  # needed for scaffolding tests
    'zope.testbrowser>=5.0.0',
]

setup(name='substancek_cms_theme',
      version='0.0.1.dev0',
      description='substancek_cms_theme',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Framework :: Pylons",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "License :: Repoze Public License",
          ],
      author='Davide Moro',
      author_email='davide.moro@gmail.com',
      url='https://github.com/substancek/substancek_cms_theme',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='substancek_cms_theme',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = substancek_cms_theme:main
      [distutils.commands]
      npm = build_commands:NpmCommand
      bower = build_commands:BowerCommand
      gulp = build_commands:GulpCommand
      """,
      extras_require={
          'tests': test_requirements,
      },
      )
