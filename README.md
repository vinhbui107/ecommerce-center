# Movie Center Website

My assignment for Information Security.

## Features

Users login, logout, change password and reset password by their email.

Update users profile.

Buy and checkout.

Security basic for website (this is a importaint fearture in this project).

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
(env) $ pip3 install -r requirements.txt
```

Run our project

```
(env) $ python manage.py runserver
```

Load the site at http://127.0.0.1:8000.
