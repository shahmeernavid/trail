Trail
======

Setup instructions:
------

1. Navigate to root directory of this repository
2. ```pip install virtualenv```
3. ```pip install virtualenvwrapper```
4. Add the following to your ```.bashrc''' file:
⋅⋅* ```export WORKON_HOME=$HOME/.virtualenvs```
⋅⋅* ```export PROJECT_HOME=$HOME/Devel```
⋅⋅* ```source /usr/local/bin/virtualenvwrapper.sh```
5. ```mkvirtualenv trail```
6. ```workon trail```
7. ```setvirtualenvproject $VIRTUAL_ENV $(pwd)```
8. ```pip install -U -r requirements.txt```