# beefy-connection

A kiosk for connecting with potential contributors and following up from event contacts.  This was created for use by the Fedora linux distribution.

## Who should use this? 

This was created for following up with conference contacts.  This could easily be expanded to job fairs, etc.  It's built with Python Flask and can use multiple RDBMS, so customizing is straightforward.

## Installation

Installing the necessary application prerequisites is as simple as:

`python setup.py install`

### Data backend

The application defauls to .sqlite, which is great for development, but there are also included configurations for other databases, such as PostgreSQL.  There is a db install script in the root to help with the initial db setup.  

## Running it

The easiest way to run the app is:

`python beefyconnection/beefyflask.py`

It's *strongly recommended* that you disable debugging and use a threaded server like gunicorn for production use.

## Under the Hood

The app is powered by Python Flask, but the UI is driven almost entirely by jquery - data is validated and parsed by javascript and then sent and handled via ajax.  The webcam capture uses WebRTC, so a recent Mozilla Firefox is recommended.  The data backend is SQL Alchemy, so it's portable between relational databases.  sqlite3 and postgreSQL were tested/targetted for initial development, but using other backends should be supported.

## What needs work/testing/tweaking (patches welcome!)

* Front-end and backend field validation
* Properly resetting all data on return to form
* Front-end error handling
* Easily turning off log/shell noise

## Features to come (patches welcome!)

* Export/import of data.
* Email confirmation, with handling for offline
* Integrating with basic config file
* If there's desire for it, NoSQL backend support
