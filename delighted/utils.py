"""
"""
import requests


class DelightedAPIError(Exception):
    """Custom expection for Delighted API related errors.

       Initialization can be done one of two ways:
        1) Passing in a 'message' kwarg with the desired error message.
        2) Passing in a 'status_code' kwarg which will result in the corresponding
           error message found in the STATUS_CODE_MESSAGES attribute.
    """
    STATUS_CODE_MESSAGES = {
        401: 'That API key is invalid.',
        406: 'That request format is invalid. Please suffix request URL with .json',
        422: 'That request is invalid.',
        500: 'A server error occured.',
        503: 'Delighted is currently down for maintenance.'}

    def __init__(self, **kwargs):
        message = kwargs.get('message', None)
        status_code = kwargs.get('status_code', None)
        if message:
            return super(DelightedAPIError, self).__init__(message)
        status_message = self.STATUS_CODE_MESSAGES.get(status_code, '')
        return super(DelightedAPIError, self).__init__(status_message)


class Resource(object):
    """Parent class for all Delighted resource types.

       Initialized with Delighted API key.

       It is important that children of this class have their RESOURCE_URL
       attributes overwritten to ensure that requests hit the expected API
       endpoint.
    """
    BASE_URL = 'https://api.delightedapp.com/v1/'
    RESOURCE_URL = ''  # To be set by children

    SUCCESS_STATUS = (200, 201)

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = '%s%s.json' % (self.BASE_URL, self.RESOURCE_URL)

    def create(self, **kwargs):
        """Create a new object with the given kwargs.

           Simply a wrapper around the post method for readability.
        """
        return self.post(**kwargs)

    def update(self, email, **kwargs):
        """Update an existing object (identified by given email) with the
           given kwargs.
        """
        kwargs['email'] = email
        return self.post(**kwargs)

    def get(self, **kwargs):
        """Send a GET request to the given endpoint with the given kwargs.
        """
        return self._make_request('get', kwargs)

    def post(self, **kwargs):
        """Send a POST request to the given endpoint with the given kwargs.
        """
        return self._make_request('post', kwargs)

    def _make_request(self, method, data={}, url=None):
        """The core method for making requests.

           Important Arguments:
            - method -> string which corresponds to the desired http method for
                        the request. Valid methods are:
                            'post', 'get', 'put', 'delete', 'head', 'options'

            - data -> dict corresponding to the key / value pairs you wish to
                      send along with the request

            - url -> url of the endpoint you would like to make a request to.
                     Defaults to the resources url attribute.

           Returns the JSON response.
        """
        url = url if url else self.url

        try:
            request_method = getattr(requests, method)
        except AttributeError:
            raise DelightedAPIError(message='Invalid request method.')

        request_data = dict(auth=(self.api_key, ''))
        if method == 'get':
            request_data['params'] = data
        else:
            request_data['data'] = data

        response = request_method(url, **request_data)

        if response.status_code not in self.SUCCESS_STATUS:
            raise DelightedAPIError(status_code=response.status_code)

        try:
            response_data = response.json()
        except TypeError:  # .json is a property for some versions of requests.
            response_data = response.json

        return response_data
