from setuptools import setup
from setuptools import find_packages

with open("./requirements.txt", "r") as req_file:
    reqs_from_req_file = req_file.read().splitlines()

setup(
        name='clam',
        version='0.1',
        description='command line telegram',
        author='gmati13',
        author_email='mati.green.13@gmail.com',
        packages=find_packages(),
        install_requires=reqs_from_req_file,

        entry_points={
            'console_scripts': [
                'clam = command_line_telegram.main:main'
            ]
        }

)
