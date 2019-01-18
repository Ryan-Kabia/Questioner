import unittest
import pytest
from flask import json
from app.api.v1.models.models import Meetups, Users, Questions, Rsvps, Comments
from app.api.tests.v1.basetest import BaseTest
from datetime import datetime

class Test_Succesful(BaseTest):
    """
    Class that asserts expected succesfull outcomes. 
    """
    def test_create_meetup(self):
        response = self.client.post('/meetups',data = json.dumps(self.meetup_input),content_type='application/json',)

        self.meetup_input.update(createdOn=datetime.utcnow().strftime("%d/%m/%Y"))
        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 201
        assert data['status'] == 201
        assert data['data'] == [self.meetup_input]

    def test_create_question(self):
        response = self.client.post('/questions',data = json.dumps(self.question_input),content_type='application/json',)

        self.question_input.update(createdOn=datetime.utcnow().strftime("%d/%m/%Y"))
        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 201
        assert data['status'] == 201
        assert data['data'] == [self.question_input]

    def test_create_comment(self):
        for entry in Questions:
            i = entry["id"]
            qstn = entry["title"]
            response = self.client.post('questions/{}/comment'.format(i), data=json.dumps(self.comment_input), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))
            self.comment_input.update(question = qstn)

            assert response.status_code == 201
            assert data['status'] == 201
            assert data['data'] == [self.comment_input]

    def test_all_meetups(self):
        response = self.client.get('/meetups/upcoming/',content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['status'] == 200
        assert data['data'] == Meetups

    def test_specific_meetups(self):
        for entry in Meetups:
            i =entry["id"]

            response = self.client.get('/meetups/{}'.format(i),content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            assert response.status_code == 200
            assert data['status'] == 200
            assert data['data'] == entry

        j = len(Meetups)+1

        response = self.client.get('/meetups/{}'.format(j),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 404
        assert data['status'] == 404
        assert data['data'] == "entry cannot be found"

    def test_upvote(self):
        for entry in Questions:
            i = entry["id"]
            meetup = entry["meetup"]
            title = entry["title"]
            body = entry["body"]
            votes = entry["votes"]+1

            rtrn = {"meetup": meetup,
                    "title": title,
                    "body": body,
                    "votes": votes
                    }

            response = self.client.patch('/questions/{}/upvote'.format(i), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            assert response.status_code == 201
            assert data['status'] == 201
            assert data['data'] == [rtrn]

    def test_downvote(self):
        for entry in Questions:
            i = entry["id"]
            meetup = entry["meetup"]
            title = entry["title"]
            body = entry["body"]
            votes = entry["votes"]-1

            rtrn = {"meetup": meetup,
                    "title": title,
                    "body": body,
                    "votes": votes
                    }

            response = self.client.patch('/questions/{}/downvote'.format(i), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            assert response.status_code == 201
            assert data['status'] == 201
            assert data['data'] == [rtrn]

    def test_rsvp(self):
        for entry in Meetups:
            topic = entry["topic"]
            i = entry["id"]

            response = self.client.post('/meetups/{}/rsvp'.format(i), data=json.dumps(self.rsvp_input),content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            
            assert response.status_code == 200
            assert data['status'] == 200
            assert data['data'] == [{"topic":topic,"meetup":i,"responce":self.rsvp_input["responce"]}]
       
class Test_empty(BaseTest):
    """
    Class that asserts empty fields get a 400 error 'one or more
    fields are empty'
    """
    def test_create_meetup_empty(self):
        self.meetup_input.update(location = "")
        response = self.client.post('/meetups', data=json.dumps(self.meetup_input), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "One of more fields are empty"

    def test_create_question_empty(self):
        self.question_input.update(body="",title = "")
        response = self.client.post('/questions', data=json.dumps(self.question_input), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "One of more fields are empty"

    def test_create_comment_empty(self):
        self.comment_input.update(responce = "")
        for entry in Questions:
            i = entry["id"]
            qstn = entry["title"]
            response = self.client.post('questions/{}/comment'.format(i), data=json.dumps(self.comment_input), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))
            self.comment_input.update(question=qstn)

            assert response.status_code == 400
            assert data['status'] == 400
            assert data['error'] == "One of more fields are empty"

    def test_rsvp_empty(self):
        self.rsvp_input.update(user="", responce="")
        for entry in Meetups:
            id = entry["id"]

            response = self.client.post('/meetups/{}/rsvp'.format(id), data=json.dumps(self.rsvp_input), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            assert response.status_code == 400
            assert data['status'] == 400
            assert data['error'] == "One of more fields are empty"

class Test_Invalid_Date(BaseTest):
    """
    Class that asserts:
        1)date for future meetup has valid format i.e dd/mm/yyyy
        2)date for a future meetup can't be prior to/same as current date
    and gives thier respective error messages
    """

    def test_create_meetup_format(self):
        self.meetup_input.update(happeningOn="2-6-2018")
        response = self.client.post(
            '/meetups', data=json.dumps(self.meetup_input), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "Bad date format. Use 'dd/mm/yyyy'"

    def test_create_meetup_invalid(self):
        self.meetup_input.update(happeningOn="2/6/2018")
        response = self.client.post('/meetups', data=json.dumps(self.meetup_input), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "Invalid Date! Cant be the same as or prior to the current date"

class Test_Rsvp_Responce(BaseTest):
    """
    Class that asserts responces to a meetup invitation are 
    restrained to 'Yes', 'No' or 'Maybe'
    """

    def test_rsvp_allowed(self):
        for responce in ["yes","YES","MayBe","NO","no","maybe"]:
            self.rsvp_input.update(responce= responce)
            for entry in Meetups:
                topic = entry["topic"]
                id = entry["id"]

                response = self.client.post('/meetups/{}/rsvp'.format(id), data=json.dumps(
                    self.rsvp_input), content_type='application/json',)

                data = json.loads(response.get_data(as_text=True))

                assert response.status_code == 200
                assert data['status'] == 200
                assert data['data'] == [{"topic": topic, "meetup": id, "responce": self.rsvp_input["responce"]}]

    def test_rsvp_not_allowed(self):
        for responce in ["Kinda", "Meh", "idk", "guess?", "prolly", "turnup!"]:
            self.rsvp_input.update(responce=responce)
            for entry in Meetups:
                id = entry["id"]

                response = self.client.post('/meetups/{}/rsvp'.format(id), data=json.dumps(
                    self.rsvp_input), content_type='application/json',)

                data = json.loads(response.get_data(as_text=True))

                assert response.status_code == 400
                assert data['status'] == 400
                assert data['error'] == "Limit Answers to:Yes, No or Maybe"







        

