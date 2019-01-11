import unittest
from app import ryan_app
from flask import json
from app.api.v1.models.models import *
import pytest


class BaseTest(unittest.TestCase):
    def setUp(self):

        last_id = Meetup[-1]["id"]
        inc_id = last_id+1

        last_id = Question[-1]["id"]
        qinc_id = last_id+1

        self.app = ryan_app
        self.client = self.app.test_client()

        self.data1 ={
            "id":inc_id,
            "createdOn": "8/1/2019",
            "location": "hilton park",
            "happeningOn":"15/2/2019",
            "topic": "What?",
            "Tags": "5w",
        }

        self.data2 = {
            "id": qinc_id,
            "createdOn": "8/1/2019",
            "createdBy": "Adam Cole",
            "meetup": 1,
            "title": "This is NXT",
            "body":"Undisputed BayBay!",
            "votes": 0,
        }


class TestCreateUser(BaseTest):
    def test_create_meetup(self):
        response = self.client.post('/meetups',data = json.dumps(self.data1),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 201
        assert data['status'] == 201
        assert data['data'] == [self.data1]

    def test_create_question(self):
        response = self.client.post('/questions',data = json.dumps(self.data2),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 201
        assert data['status'] == 201
        assert data['data'] == [self.data2]

    def test_all_meetups(self):
        response = self.client.get('/meetups/upcoming/',content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['status'] == 200
        assert data['data'] == Meetup

    def test_specific_meetups(self):
        for entry in Meetup:
            i =entry["id"]

            response = self.client.get('/meetups/{}'.format(i),content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            assert response.status_code == 200
            assert data['status'] == 200
            assert data['data'] == entry

        j = Meetup[-1]["id"]+1

        response = self.client.get('/meetups/{}'.format(j),content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 404
        assert data['status'] == 404
        assert data['data'] == "entry cannot be found"

    def test_upvote(self):
        for entry in Question:
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
        for entry in Question:
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

        

