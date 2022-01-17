from setuptools import setup, find_packages

setup(
    name='LandsatGEEPy',
    packages=find_packages(),
    include_package_data=True,
    version='0.0.1',
    description='Helper functions for Landsat processsing with GEE',
    url='https://github.com/BuddyVolly/LandsatGEEPy',
    author='Andreas Vollrath',
    author_email='andreas.vollrath[at]fao.org',
    license='MIT License',
    keywords=['Landsat', 'USGS',
              'Earth Observation', 'Remote Sensing',
              'Google Earth Engine'],
    zip_safe=False,
)