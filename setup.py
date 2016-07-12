import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='modelowneradmin',
    version='1.0',
    install_requires=[
        'django>=1.5',
        'django_extras',
    ],
    packages=find_packages(),
    include_package_data=True,
    license='GNU GPLv3',
    description='A Django ModelAdmin to restrict model access to owners.',
    long_description=README,
    url='https://adarnauth.com/',
    author='Adarnof',
    author_email='adarnof@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GPLv3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
