beefy-connection
================

A kiosk for connecting with potential contributors and following up from event contacts.  This was created for use by the Fedora linux distribution.

** Who should use this? **

This was created for following up with conference contacts.  This could easily be expanded to job fairs, etc.  It's built with Python Flask and can use multiple RDBMS, so customizing is straightforward.

** Installation **

Installing the necessary application prerequisites is as simple as:

`python setup.py install`

The application defauls to .sqlite, which is great for development, but there are also included configurations for other databases, such as PostgreSQL.  There is a db install script in the root to help with the initial db setup.  

The easiest way to run the app is:

`python beefyconnection/beefyflask.py`

It's strongly recommended that you disable debugging and use a threaded server like gunicorn for production use.

** Under the Hood **

The app is powered by Python Flask, but the form page is driven by jquery.  The webcam capture uses WebRTC, so a recent Mozilla Firefox is recommended.  The data backend is SQaLchemy, so it's portable between relational databases.
