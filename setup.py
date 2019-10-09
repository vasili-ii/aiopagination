#!/usr/bin/env python
from setuptools import setup


setup(name='aiopagination',
      version='0.0.1',
      description='Simple pagination for aiohttp-server',
      author='Vasiliy Sidorov',
      author_email='vasili.sidorov@gmail.com',
      url='https://github.com/vasili-ii/aiopagination',
      packages=['aiohttp'],
      install_requires=['sqlalchemy'],
      license='MIT',
      classifiers=['Intended Audience :: Developers',
                   'Topic :: Software Development :: Libraries',
                   'Development Status :: 3 - Alpha',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   ])
