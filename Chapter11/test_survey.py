import unittest
from survey import AnonyousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test for Anonyous object"""

    def setUp(self):
        """
        create an survey and a pair of answer,
        for your test
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonyousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    def test_store_single_response(self):
        """test single response will be saved correctly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn("English", self.my_survey.responses)

    def test_store_three_responses(self):
        """test three responses will be saved correctly"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

        
