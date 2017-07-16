[![Build Status](https://travis-ci.org/ocadotechnology/codeforlife-portal.svg?branch=master)](https://travis-ci.org/ocadotechnology/codeforlife-portal)
[![Coverage Status](https://coveralls.io/repos/ocadotechnology/codeforlife-portal/badge.svg?branch=master&service=github)](https://coveralls.io/github/ocadotechnology/codeforlife-portal?branch=master)
[![Code Climate](https://codeclimate.com/github/ocadotechnology/codeforlife-portal/badges/gpa.svg)](https://codeclimate.com/github/ocadotechnology/codeforlife-portal)

## A  [Code for Life](https://www.codeforlife.education/) repository
* Ocado Technology's [Code for Life initiative](https://www.codeforlife.education/) has been developed to inspire the next generation of computer scientists and to help teachers deliver the computing curriculum.
* This repository hosts the source code of the **main website**: the portal for the Code For Life initiative, the registration/log in, the teachers' dashboards, the teaching materials, etc
* The other repos for Code For Life:
    * the first game, [Rapid Router](https://github.com/ocadotechnology/rapid-router)
    * the new game for teenagers, [currently at a very early stage](https://github.com/ocadotechnology/aimmo)
    * the [deployment code for Google App Engine](https://github.com/ocadotechnology/codeforlife-deploy-appengine)

## Running Locally
* Clone the repo
* Install prerequisites. E.g. on Ubuntu / Linux Mint:
    * `sudo apt-get install git`
    * `sudo apt-get install python-dev`
    * `sudo pip install virtualenvwrapper`
    * `sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev`
    * `sudo apt-get install ruby2.0` - still Ruby 1.9 hiding under `ruby` command.
    * `sudo gem install sass -v 3.3.4` - later versions incompatible with Ruby 1.9 (see above).
* Make and activate a virtualenv (We recommend [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html))
    * e.g. the first time, `mkvirtualenv -a path/to/codeforlife-portal codeforlife-portal`
    * and thereafter `workon codeforlife-portal`
    * create settings file under `example_project/example_project/local_settings.py` with `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
* `./run` - This will:
    * install all of the dependencies using pip
    * sync the database
    * collect the static files
    * run the server
* Once you see `Quit the server with CONTROL-C`, you can open the portal in your browser at `localhost:8000`.

* If you have problems seeing the portal on machines with different locale (e.g. Polish), check the terminal for errors mentioning `ValueError: unknown locale: UTF-8`. If you see them, you need to have environment variables `LANG` and `LC_ALL` both set to `en_US.UTF-8`.
    * Either export them in your `.bashrc` or `.bash_profile`
    * or restart the portal with command `LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 ./run`.

## How to contribute!
__Want to help?__ You can contact us using this [contact form][c4l-contact-form] and we'll get in touch as soon as possible! Thanks a lot.

## Common Problems
### Unapplied migrations on first run
It may be that some migrations were changed and you have .pyc files from the old ones. Try removing all .pyc migrations by running `rm migrations/*.pyc` from the ocargo repository.

[c4l-contact-form]: https://www.codeforlife.education/help/#contact
