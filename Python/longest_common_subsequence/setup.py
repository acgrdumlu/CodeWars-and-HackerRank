try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'CodeWars Longest Common Subsequence',
    'author': 'Josh Peng',
    'url': 'https://github.com/joshpeng/CodeWars-and-HackerRank',
    'version': '0.1',
    'install_requires': ['nose'],
    'name': 'longest_common_subsequence'
}

setup(**config)
