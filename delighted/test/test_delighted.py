"""Basic Unit Tests for the Delighted Wrapper
"""
import unittest
import uuid


from .. import Delighted


class TestResourceBase(unittest.TestCase):
    """Base class for all resource test cases.

       Here we initialize the client using a test api key and autocreate a
       unique email address for each test we run.
    """
    def setUp(self):
        self.client = Delighted('<your_test_api_key_here>')
        self.test_email = 'test+%s@gmail.com' % (uuid.uuid4())


class TestPersonResource(TestResourceBase):
    """Tests for Person resource methods.
    """
    def test_person_is_created_correctly(self):
        response = self.client.person.create(email=self.test_email)
        self.assertEqual(type(response), dict)
        self.assertEqual(response['email'], self.test_email)

    def test_person_can_be_updated(self):
        response1 = self.client.person.create(email=self.test_email)
        self.assertEqual(response1['properties'], {})

        response2 = self.client.person.update(
            self.test_email, properties={'location': 'Boston', 'user_type': 'human'})
        self.assertEqual(response2['properties']['location'], 'Boston')
        self.assertEqual(response2['properties']['user_type'], 'human')

    def test_scheduled_surveys_can_be_deleted(self):
        self.client.person.create(email=self.test_email)

        response = self.client.person.delete(self.test_email)
        self.assertEqual(response['ok'], True)


class TestSurveyResponseResource(TestResourceBase):
    """Tests for Survey Response resource methods.
    """
    def test_survey_response_is_created_correctly(self):
        ## First create a new Person
        response1 = self.client.person.create(email=self.test_email)
        person_id = response1['id']

        response2 = self.client.survey_response.create(
            person=person_id, score=10, comment='What a great app!')

        self.assertEqual(type(response2), dict)
        self.assertEqual(response2['person'], person_id)
        self.assertEqual(response2['score'], 10)
        self.assertEqual(response2['comment'], 'What a great app!')

    def test_survey_responses_can_be_retrieved_correctly(self):
        response = self.client.survey_response.get()
        self.assertEqual(type(response), list)
        if len(response) > 0:
            self.assert_('person' in response[0])
            self.assert_('score' in response[0])
            self.assert_('comment' in response[0])

class TestMetricsResource(TestResourceBase):
    """Tests for Metrics resource methods.
    """
    def test_metrics_can_be_retrieved_correctly(self):
        response = self.client.metrics.get()
        self.assertEqual(type(response), dict)
        self.assert_('nps' in response)


if __name__ == '__main__':
    unittest.main()
