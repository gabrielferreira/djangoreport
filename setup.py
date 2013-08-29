from setuptools import setup, find_packages
import os

version = __import__('djangoreport').__version__

def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "djangoreport",
    version = version,
    url = 'http://github.com/',
    license = '',
    platforms=['OS Independent'],
    description = "",
    long_description = read('README.md'),
    author = '',
    author_email = '',
    packages=find_packages(),
    install_requires = (
        'Django==1.5.2',
        'South==0.8.2',
        'wsgiref==0.1.2',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 1 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
    ),
)