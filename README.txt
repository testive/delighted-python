================
Delighted Python
================

Python wrapper for the `Delighted API <https://delightedapp.com/docs/api>`_.

Getting started is easy!::

    from delighted import Delighted

    ## Initialize with API Key
    client = Delighted('<your_api_key_here>')

  	## Get a list of all survey responses
  	responses = client.survey_responses.get()
