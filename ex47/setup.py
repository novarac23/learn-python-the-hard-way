try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project'.
    'author': 'Nikola Novakovic',
    'url': 'URL to get it at',
    'download_url': 'where to download it',
    'author_email': 'my_email',
    'version': '0.1',
    'install_requires': ['nose'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
