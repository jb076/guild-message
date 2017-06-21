# Guild Message
A demo project for Guild Education.  It's a simple messenger application.

# Setup
1.  Install python 3 if not already installed.
2.  [Install virtualenv wrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)
3.  Create virtual env ```mkvirtualenv --python=<-path to Python eg:/usr/bin/python3-> <name>```
4.  Install Requirements
```
cd <repo base dir>
pip install -r requirements.txt
```

5. Run migrations
```
python manage.py migrate
```
6. Run included onetime script to give you the semi-hardcoded users
```
# From Base Repo
python ./guild_message/onetime_scripts/add_test_users.py

```
7.  Run Server ```python manage.py runserver```


# Development Thoughts
## Why Django
In the interest of keeping things within the scope of the guidelines, I decided to put this together in the tech I knew best in order to be able to submit a working product within the time frame suggested.

I'll be polling the server in order to update messages.  For production software, this is less than ideal.  In practice, something with better socket support (node + socket.io), or even SSE support, would be best to minimize delay between updates and enable nifty features like "user is typing" feedback to recipient.  Time permitting, I would like to explore a project which leverages Redis to give socket and better long polling support.

## In Progress
1. Currently ignoring ability to edit previous messages (eg: slack).  Would need to add a last_edit date, or maybe re-getting past messages.

2. In another world, I'd probably end up building this out with a proper RESTful API and self-consume.  Gives the option for people to write their own clients, decouples the overall architecture.  Just not going to worry about auth tokens etc right now.

3. "New Message" feature might be nice.

4. Wishing I had named Messenger "Messages."  As we used to say in my old office "naming is hard..."

5.  I really do not like tying conversations to user-receiver.  Instead, I think messages would be better with a "conversation."  *Ended up just doing this.

6. Potential timing issue with updates.  I wanted to show entered messages ASAP, and since I am polling, I did not want to wait for next request.  However, with the way last message is working, this could potentially cause an issue where users enter messages and more or less the same time and a message would be missed.

7.  Better statuses/structured packages in the future would be beneficial.

8. I ended up not using bootstrap.  In keeping with the guidelines, I kept the visuals pretty simple so it was just easier to throw a few basic styles together.

9.  Would probably do some more tests.  Last message ranged requests would be especially important, but really just overall coverage.  I used TDD just getting the endpoints up and running but then ran away with development on the details so tests did not end up where I'd consider to be "good coverage."