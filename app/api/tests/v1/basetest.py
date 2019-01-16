import unittest
from app.api.v1.models.models import Meetups,Users,Questions,Rsvps,Comments
from app import ryan_app



class BaseTest(unittest.TestCase):
    def setUp(self):

        last_id = len(Meetups)+1
        meetup_plus_id = last_id

        last_id = len(Questions)+1
        question_plus_id = last_id

        last_id = len(Rsvps)+1
        rsvp_plus_id = last_id

        last_id = len(Comments)+1
        comment_plus_id = last_id


        self.app = ryan_app
        self.client = self.app.test_client()

        self.meetup_input = {
            "id":meetup_plus_id,
            "location": "hilton park",
            "happeningOn": "15/2/2019",
            "topic": "What?",
            "Tags": "5w",
        }

        self.question_input = {
            "id": question_plus_id,
            "createdBy": "Adam Cole",
            "meetup": 1,
            "title": "This is NXT",
            "body": "Undisputed BayBay!",
            "votes": 0,
        }

        self.rsvp_input = {
            "id": rsvp_plus_id,
            "user": "Adam Cole",
            "responce": "Maybe",
        }

        self.comment_input = {
            "id": comment_plus_id,
            "user": "Adam Cole",
            "responce": "You love it!"
        }

        
