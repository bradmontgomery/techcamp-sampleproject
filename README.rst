Sample Django Project
=====================

This is a sample django project, a portion of which was demo'ed at TechCamp
Memphis, Nov. 2012.

*WARNING*: This is a whole project. You'd typically generate your own project
directory and then build your own apps. If you *do* decide to use/deploy this,
read through the ``settings.py`` file and change things to suite your needs 
(particularly the ``SECRET_KEY`` value).


Deploying to Heroku
-------------------

Once you've got the `Heroku Toolbelt <http://goo.gl/RHccU>`_ installed, you
need to do the following:

* Make sure you have a virtualenv that meets the
  `prerequisites <https://devcenter.heroku.com/articles/django>`_, including
  a ``requirements.txt`` file.
* Create a heroku app::
    
    $ heroku create

  Output should look something like this::

    Creating nameless-atoll-5495... done, stack is cedar
    http://nameless-atoll-5495.herokuapp.com/ | git@heroku.com:nameless-atoll-5495.git
    Git remote heroku added

* Deploy your app::
    
    $ git push heroku master

* Run ``syncdb``::

    $ heroku run python manage.py syncdb

* Edit your app (do development locally). When you're ready to re-deploy::

    $ git push heroku master


Static Media
------------

A quick note on static media (css, js, images, etc). These don't get stored
on Heroku. Host them on a service intended to serve static content. Good
options for this include:

* Amazon S3
* Rackspace CloudFiles
* A linux box with a plain-ole webserver (nginx or apache). A cheap shared
  hosting service is also good for this.

