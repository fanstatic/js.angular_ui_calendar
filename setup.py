from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '0.9.0.dev0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'angular_ui_calendar', 'test_angular-ui_ui-calendar.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.angular_ui_calendar',
    version=version,
    description="Fanstatic packaging of angular-ui ui-calendar",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    license='BSD',
    packages=find_packages(),namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        'js.angular',
        'js.fullcalendar >= 2.0',
        ],
    entry_points={
        'fanstatic.libraries': [
            'angular-ui-calendar = js.angular_ui_calendar:library',
            ],
        },
    )
