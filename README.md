# Guild Message
A demo project for Guild Education.  It's a simple messenger application.

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
In the interest of keeping things within the scope of the guidelines, I decided to put this together in the tech I knew best in order to be able to submit a working product within the time frame suggested.

I'll be polling the server in order to update messages.  For production software, this is less than ideal.  In practice, something with better socket support (node + socket.io), or even SSE support, would be best to minimize delay between updates and enable nifty features like "user is typing" feedback to recipient.  Time permitting, I would like to explore a project which leverages REDIS to give socket and better long polling support.

## In Progress
1. Currently ignoring ability to edit previous messages (eg: slack).  Would need to add a last_edit date, or maybe re-getting past messages.

2. In another world, I'd probably end up building this out with a proper RESTful API and self-consume.  Gives the option for people to write their own clients, decouples the overall architecture.  Just not going to worry about auth tokens right now...

3. "New" feature might be nice.

4. Wishing I had named Messenger "Messages."  As we used to say in my old office "naming is hard..."

5.  I really do not like tying conversations to user-receiver.  Instead, I think messages would be better with a "conversation"	