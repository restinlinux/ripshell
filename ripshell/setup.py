from setuptools import find_packages, setup, version

setup(
    name='ripshell',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
        'rich'
        'pyfiglet'
        'termcolor'
    
    ],
    entry_points='''
    [console_scripts]
    ripshell=ripshellcli:ripshellcli
    '''

)
