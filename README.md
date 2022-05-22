# Blurgo

## 1. Purpose

Blurgo at its core is a memory game. The aim is to guess the "logo of the day" with a blur filter applied. The filter will slowly reduce over a 2 minute time frame. The player's score is calculated based on the time taken and the number of attempted guesses. A new random logo is released every day, and players can compare their scores in the results table.

Memory-based games are a fun method of exercising the mind, being known to improve brain functions such as memory-recollection, concentration, and focus.

The other aspect of this game is to challenge the way we identify patterns in the recognition of brands. Many brands market themselves profusely in every aspect of our lives, and the patterns of the most easily recognisable brands can be learnt from the results generated from the app. This data could potentially be used in machine learning applications to identify common themes amongst the most recognisable brands, traits identifiable even when obfuscated by a blurring filter.

## 2. Architecture

This web application was built with HTML, CSS (with styling primarily built upon Bootstrap functionalities), Javascript and Python (Flask). The dependencies can be found in ***requirements.txt***. It uses Flask modules such as Flask-login and Flask-SQLAlchemy to manage the user database and WTForms to validate the login/sign-up pages.

## 3. Installation / How To Launch

NOTE: This process assumes the user has Python and pip installed

- Python >= 3.8, installed as either *python* or *python3*
  - an easy way to check which version you are on, is to run:

```sh
$ python -V
# or if  you have Python 2 installed as your default Path name for python, run python3 instead (we will be using python3 from now on)
$ python3 -V
```

- Pip >= 22.1
  - Same as above, check the version of your pip by running:

```sh
$ pip3 -V
```

Within the **Agile-Project-2022** directory:

```sh
# Recommended for MacOS / Linux
$ python3 -m venv venv && source venv/bin/activate

# Or when running on Windows
$ python3 -m venv venv && source venv/Scripts/activate

# Then run the following to install all the dependencies
$ pip3 install -r requirements.txt
```

To launch the application, run the following command:

```sh
$ flask run
```

The web application should now be running at http://127.0.0.1:5000/

## 4. Describe some unit tests for the web application, and how to run them

There are some tests stored within the */tests/unittest.py* file. 
You can run the command:

```sh
$ python3 -m unittest -v tests/unittest.py
```

## 5. Include commit logs, showing contributions and review from both contributing students
  
Commit logs can be found under the git commit file.

## 6. Resources Used

A big thank you to the following resources used in the production of this web-app:

- [Figma](https://www.figma.com/file/tn4Bsz7LHcRCxrgEauJxAj/Blurgo-Figma-Board?node-id=0%3A1)

- [Github](https://github.com/mattshroom/Agile-Project-2022)

- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

- [Github PR Template](https://embeddedartistry.com/blog/2017/08/04/a-github-pull-request-template-for-your-projects/)

- [CSS Tricks](https://css-tricks.com/)

- [Codesource](https://codesource.io/building-a-restful-crud-api-with-flask/)
 
## 7. Authors

Matthaeus Ong, Cameron Nguyen, Lachlan Bassi, Nicholas Chua
