from setuptools import find_packages, setup

# packages tells Python what package directories (and the Python files they contain) to include.
# find_packages() finds these directories automatically so you don’t have to type them out.
#
# To include other files, such as the static and templates directories,
# include_package_data is set.
# Python needs another file named MANIFEST.in to tell what this other data is.
setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

# See the official packaging guide
# [on https://packaging.python.org/tutorials/packaging-projects/]
# for another explanation of the files and options used.

'''
Use pip to install your project in the virtual environment.

$ pip install -e .

This tells pip to find setup.py in the current directory
and install it in editable or development mode.
Editable mode means that as you make changes to your local code,
you’ll only need to re-install if you change the metadata about the project,
such as its dependencies.

...

Nothing changes from how you’ve been running your project so far.
FLASK_APP is still set to flaskr and `flask run` still runs the application,
but you can call it from anywhere, not just the flask-tutorial directory.
'''