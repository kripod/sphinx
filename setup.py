from setuptools import setup

import sphinxmix

setup(name='sphinxmix',
      version=sphinxmix.VERSION,
      description='A Python implementation of the Sphinx mix packet format.',
      author='George Danezis',
      author_email='g.danezis@ucl.ac.uk',
      url=r'https://pypi.python.org/pypi/sphinxmix/',
      packages=['sphinxmix'],
      license="2-clause BSD",
      long_description="""A Python implementation of the Sphinx mix packet format.""",

      setup_requires=["pytest >= 2.6.4"],
      install_requires=[
            "future >= 0.14.3",
            "pytest >= 2.6.4",
            "msgpack-python >= 0.4.6",
            "petlib >= 0.0.38",
            "numpy >= 1.11.0",
      ]
)