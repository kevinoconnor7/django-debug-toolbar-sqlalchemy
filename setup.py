from setuptools import setup, find_packages
from debug_toolbar_sqlalchemy import __version__

setup(
    name='django-debug-toolbar-sqlalchemy',
    version=__version__,
    description='SQLAlchemy query information panel for Django Debug Toolbar',
    long_description=open('README.md').read(),
    author='Kevin O\'Connor',
    author_email='kevin@oconnor.mp',
    url='https://github.com/kevinoconnor7/django-debug-toolbar-sqlalchemy',
    license='GPLv3',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
