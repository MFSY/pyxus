import os
from optparse import Option

import pip
from setuptools import setup
from pip.req import parse_requirements

try:
    import pypandoc
    long_description = pypandoc.convert('../README.md', 'rst')
except(IOError, ImportError):
    long_description = open('../README.md').read()

# This is a hack to work with newer versions of pip
if (pip.__version__.startswith('1.5') or
   int(pip.__version__[:1]) > 5):
    from pip.download import PipSession  # pylint:disable=E0611
    OPTIONS = Option("--workaround")
    OPTIONS.skip_requirements_regex = None
    OPTIONS.isolated_mode = False
    # pylint:disable=E1123
    INSTALL_REQS = parse_requirements(os.path.join(os.path.dirname(__file__), "requirements.txt"),
                                      options=OPTIONS,
                                      session=PipSession)
else:  # this is the production path, running on RHEL
    OPTIONS = Option("--workaround")
    OPTIONS.skip_requirements_regex = None
    INSTALL_REQS = parse_requirements(os.path.join(os.path.dirname(__file__), "requirements.txt"),
                                      options=OPTIONS)

reqs = [str(ir.req) for ir in INSTALL_REQS]


setup(
    name='pyxus',
    version='0.1.3',
    packages=['pyxus', 'pyxus.resources', 'pyxus.utils'],
    install_requires = reqs,
    author='HumanBrainProject',
    scripts=['manage.py'],
    author_email = 'platform@humanbrainproject.eu',
    keywords = ['pyxus', 'nexus'],
    classifiers = [],
    url = 'https://github.com/HumanBrainProject/pyxus',
    download_url = 'https://github.com/HumanBrainProject/pyxus/archive/master.zip',
    long_description = long_description

)