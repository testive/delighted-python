================
Delighted Python
================

Python wrapper for the `Delighted API <https://delightedapp.com/docs/api>`_. Get
your pythonic NPS on!

Getting started is easy!
-----------------------

Install from pip::

    sudo pip install DelightedPython

Basic Usage::

    from delighted import Delighted

    ## Initialize with API Key
    client = Delighted('<your_api_key_here>')

    ## Get a list of all survey responses
    responses = client.survey_response.get()

Person Resource
---------------

See `the docs <https://delightedapp.com/docs/api>`_ for valid parameters and usage.

People Resource Examples::

    ## Create a new person on delighted
    client.person.create(email='getmynps@testing.com')

    ## Update a person record
    client.person.update('getmynps@testing.com',
                         properties={'location': 'Boston'})

    ## Delete upcoming survey request for the given person
    client.person.delete('getmynps@testing.com')

Survey Response Resource
------------------------

See `the docs <https://delightedapp.com/docs/api>`_ for valid parameters and usage.

Survey Response Resource Examples::

    ## Post new response
    client.survey_response.create(person=123, score=10, comment='What a great app!')

    ## List all responses
    client.survey_response.get()


Metrics Resource
----------------

See `the docs <https://delightedapp.com/docs/api>`_ for valid parameters and usage.

Metrics Resource Examples::

    ## Get NPS Metrics
    client.metrics.get()

    ## Get NPS Metrics by Trend
    client.metrics.get(trend=456)


Unit Tests
----------

To run unit test first add your test api key to delighted/test/test_delighted.py.

Then run the following::

    python -m delighted.test.test_delighted


Important TODO's
----------------

1. Rework error throwing to be a bit more useful (see DelightedAPIError)


Acknowledgements
----------------

- The `Delighted <https://delightedapp.com/>`_ Team for creating a wonderful service and kick ass API
- Team `Testive <http://www.testive.com/>`_ for supporting the creation and open source of the wrapper
