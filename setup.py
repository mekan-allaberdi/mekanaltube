#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import setuptools

__version__ = '0.1'

config = {
    'name': 'mytube',
    'author': 'Mekan ALLABERDIYEV <mekan.allaberdi@gmail.com>',
    'author_email': 'mekan.allaberdi@gmail.com',
    'version': __version__,
    'install_requires': ['flask', 'pymongo', 'gunicorn', 'jinja2',
                         'dnspython', 'click'],
    'tests_require': ['nose'],
    'include_package_data': True,
    'zip_safe': False,
    'scripts': [],
    'entry_points': {
        'console_scripts': [
            'cweb=mytube.web:run_web'
        ]
    }
}

print('MyTube Version: %s' % __version__)

packages = setuptools.find_packages()
config['packages'] = packages
setuptools.setup(**config)
