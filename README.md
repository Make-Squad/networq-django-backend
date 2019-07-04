
# 🤝 networq

- Check it out: [Networq v0 Live](http://networq.herokuapp.com/)
- The live version of this product is hosted on Heroku.

## Getting Started

To install this project:

- clone this repository (run `git clone https://github.com/Make-Squad/networq-django-backend.git networq`)
- create and activate your virtual environment (run `virtualenv -p python3 venv && source venv/bin/activate` from the root folder)
- install the requirements by running `pip install -r requirements.txt` from the root folder (you might need to comment out `django-heroku` if you're using a Mac)
- run the server by running `python manage.py runserver`

## Current Build

This project is built with Django 2.2.2. All versions for our dependancies are listed in requirements.txt. To install dependencies, run `pip install -r requirements.txt` from the root folder.

## File Structure 🗂

This projects currently consists of three apps: cards, users and api.

```
root/ (networq)
|
|-- networq/
|---- settings.py
|
|-- cards/
|-- users/
|-- api/
|
|-- README.md
|-- proposal.md (project proposal)
|
|-- requirements.txt
|-- Procfile
|-- manage.py
|-- .gitignore
```

## Testing 📝

Testing is done using Django Test Framework. To run our tests, please run `./manage.py test` from the root folder.

## Endpoints

- /users - view a list of all users
- /users/username - view a single user by username
- /cards - view a list of all cards
- /cards/card_id - view a single card by id

- /api/users - DJANGO REST framework api list view of all users
- /api/users/username - DJANGO REST framework api detail view of one user (WIP)
- /api/cards - DJANGO REST framework api list view of all cards
- /api/cards/card_id - DJANGO REST framework api detail view of one user (WIP)

## Additional Contact Info ☎

For questions related to networq please email Faith Chikwekwe at faithchikwekwe01@gmail.com.

## Contributors

- [Stephanie Cherubin](http://github.com/stephanieCherubin/)
- [Faith Chikwekwe](http://github.com/fchikwekwe/)
