from setuptools import setup, find_packages

from model_wrappers import __version__

extra_test = [
    'pytest>=4',
    'pytest-cov>=2',
    'pytest-django>=3',
    'psycopg2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='django-model-wrappers',
    version=__version__,

    url='https://github.com/SelfHacked/django-model-wrappers',
    author='SelfHacked',
    author_email='zheng@selfdecode.com',

    python_requires='>=3.6',

    install_requires=[
        'Django>=2',
        'returns-decorator',
    ],

    extras_require={
        'test': extra_test,
        'dev': extra_dev,

        'ci': extra_ci,
    },

    packages=find_packages(),

    classifiers=[
        'Intended Audience :: Developers',

        'Development Status :: 3 - Alpha',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',

        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',

        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
