# Movie Center Website

My assignment for Information Security 🚀.

Video demo about this project. [Watch it](https://www.youtube.com/watch?v=tolvKYo0VjY).

## Features

* Users login, logout, change password and reset password by their email.

* Update users profile.

* Search, add movie to cart and checkout.

* Security for website.

## Third-Party Packages

* [x] [django-allauth](https://github.com/pennersr/django-allauth) for social authentication
* [x] [Bootstrap](https://github.com/twbs/bootstrap) for styling
* [x] [Jquery](https://github.com/jquery/jquery)
* [x] [Font-awesome](https://github.com/FortAwesome/Font-Awesome) for icon fonts
* [x] [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) for debugging
* [x] [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) for DRY forms
* [x] [sorl-thumbnail](https://github.com/jazzband/sorl-thumbnail) for thumbnail images
* [x] [python-decouple](https://github.com/henriquebastos/python-decouple/) Storing application settings
* [x] [dj-database-url](https://github.com/jacobian/dj-database-url) Storing application settings

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure Python 3.8.x, Pip and Virtualenv are already installed. [See here for help](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)

### Installing

Clone and move to project

```
$ git clone https://github.com/vinhbui107/MovieCenter.git
$ cd MovieCenter
```

Create virtual environment

```
$ virtualenv env
```

Run virtual environment

```
$ .\env\Scripts\activate
```

Install python packages for project

```
(env) $ pip install -r requirements.txt
```

Run our project

```
(env) $ python manage.py runserver
```

Load the site at http://127.0.0.1:8000.

## Tech Specs

* Python 3.8
* Django 3.0.5
* dj-database-url 0.5.0
* django-allauth 0.41.0
* django-crispy-forms 1.9.0
* Bootstrap 4.3.1
* jQuery 3.4.1
* Font Awesome 5.11.2
* python-decouple 3.3
* Pillow 7.0.0
* sorl-thumbnail 12.6.3
* django-debug-toolbar 2.2
