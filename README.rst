=====
realty
=====
export PYTHONPATH="$HOME/code/mylibraries/python"

realty is a Django app to accompany the python getrealty program

Quick start
-----------

1. Add "realty" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'realty',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('realty/', include('realty.urls')),

3. Run `python manage.py migrate` to create the realty models.

4. Visit http://127.0.0.1:8000/realty to view realty data
