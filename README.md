People Skills For Geeks
=======================

For now: Give feedback! Receive feedback!

In the future: Who knows...

Install
=======

Install Python3, pip, and set up a virtualenv. Install requirements:

    pip install -r requirements.txt

Copy `psfg/local_settings.py.template` to `psfg/local_settings.py` and change
the settings to your needs.

Don't commit migrations in the repo until go live, instead, generate them on
the fly:

    python manage.py makemigrations

Run migrations:

    python manage.py migrate

Start the dev server:

    python manage.py runserver

See the site at http://127.0.0.1:8000/
