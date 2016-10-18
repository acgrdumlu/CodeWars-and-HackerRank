try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'HackerRank Even Tree',
    'author': 'Josh Peng',
    'url': 'https://github.com/joshpeng/CodeWars-and-HackerRank',
    'version': '0.1',
    'install_requires': ['nose'],
    'name': 'even_tree'
}

setup(**config)
