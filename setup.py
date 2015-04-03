from setuptools import setup

setup(
    name='pytest-runfailed',
    license='BSD',
    description='implement a --failed option for pytest',
    version='0.5',
    author='Dimitri Merejkowsky',
    author_email='d.merej@gmail.com',
    url='http://github.com/dmerejkowsky/pytest-runfailed',
    py_modules=['pytest_runfailed'],
    entry_points={'pytest11': ['runfailed = pytest_runfailed']},
    install_requires=['pytest>=2.0'],
    classifiers=[
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ]
)
