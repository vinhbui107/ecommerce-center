# Movie Center Website

My assignment for Information Security.

## Features

Users login, logout, change password and reset password by their email.

Update users profile.

Add movie to cart and checkout.

Basic security for website (this is a importaint feature in this project).

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
