"""
"""
from utils import Resource


class Delighted(object):
    """Wrapper class for the Delighted API.

       Initialized with Delighted api_key.
    """
    def __init__(self, api_key):
        self.person = Person(api_key)
        self.survey_response = SurveyResponse(api_key)
        self.metrics = Metrics(api_key)


class Person(Resource):
    """Allows access to Delightful Person resources.

       Valid parameters for GET / POSTING can found at:
       https://delightedapp.com/docs/api
    """
    RESOURCE_URL = 'people'

    def delete(self, person_email):
        """Allows for the deletion of scheduled surveys for the given email
           address.

           Note: The url for this endpoint is a little funky, but obviously
                 belongs in the Person resource, hence the overwrite.
        """
        url = '%s%s/%s/survey_requests/pending.json' % (
            self.BASE_URL, self.RESOURCE_URL, person_email)
        return self._make_request('delete', url=url)


class SurveyResponse(Resource):
    """Allows access to Delightful SurveyResponse resources.

       Valid parameters for GET / POSTING can found at:
       https://delightedapp.com/docs/api
    """
    RESOURCE_URL = 'survey_responses'


class Metrics(Resource):
    """Allows access to Delightful Metrics resources.

       Valid parameters for GET / POSTING can found at:
       https://delightedapp.com/docs/api
    """
    RESOURCE_URL = 'metrics'
