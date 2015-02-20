People Skills For Geeks
=======================

For now: Give feedback! Receive feedback!

In the future: Who knows...

Install
=======

Install Python3, pip, then install requirements:

    pip install -r requirements.txt

Don't commit migrations in the repo until go live, instead, generate them on
the fly:

    python manage.py makemigrations

Run migrations:

    python manage.py migrate

Run the dev server:

    python manage.py runserver
