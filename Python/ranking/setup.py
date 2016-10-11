try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'CodeWars Ranking',
    'author': 'Josh Peng',
    'url': 'https://github.com/joshpeng/CodeWars',
    'version': '0.1',
    'install_requires': ['nose'],
    'name': 'ranking'
}

setup(**config)
