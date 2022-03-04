from setuptools import find_packages, setup
setup(
    name='daemon_supervisor',
    packages=find_packages(include=['daemon_supervisor']),
    version='0.0.1',
    description='Daemon Supervisor Project',
    author='Oscar Villarraga',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)