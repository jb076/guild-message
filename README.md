# Guild Message
A demo project for Guild Education.  It's a simple messanger application.

# Setup
1.  Install python 3 if not already installed.
2.  Install virtualenv wrapper
3.  Create virtual env ```mkvirtualenv <name>```
4.  Install Requirements
```
cd <repo base dir>
pip install -r requirements.txt
```
5.  Runserver ```python manage.py runserver```

# Development Thoughts
## Why Django
In the interest of keeping things within the scope of the guidelines, I decided to put this together in the tech I knew best in order to be able to submit a working product within the timeframe suggested.

I'll be polling the server in order to update messages.  For production software, this is less than ideal.  In practice, something with better socket support (node + socket.io), or even SSE, would be best to minimize delay between updates and enable nifty features like "user is typing" feedback to recepient.  Time permitting, I would like to explore a project which leverages REDIS to give socket and better long polling support.

## In Progress
1. While Django has pretty good built in support for a RESTful api via rest_framework, I'll be handling it myself.  It's a simple, single endpoint and leaning too heavily on the frameworks seems out of the spirit of the task.

2. Currently ignoring ability to edit previous messages (eg: slack).  Would need to add a last_edit date, or maybe regetting past messages.

3. "New" feature might be nice.