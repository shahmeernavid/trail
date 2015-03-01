Trail
======

Setup instructions:
------

1. Navigate to root directory of this repository
2. ```pip install virtualenv```
3. ```pip install virtualenvwrapper```
4. ```npm install```
5. Add the following to your ```.bashrc``` file:
  * ```export WORKON_HOME=$HOME/.virtualenvs```
  * ```export PROJECT_HOME=$HOME/Devel```
  * ```source /usr/local/bin/virtualenvwrapper.sh```
6. ```mkvirtualenv trail```
7. ```workon trail```
8. ```setvirtualenvproject $VIRTUAL_ENV $(pwd)```
9. ```pip install -U -r requirements.txt```


Run instructions:
------
```npm start```