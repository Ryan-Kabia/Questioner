import unittest
from app import ryan_app
from flask import json
from app.api.v1.models.models import *
import pytest


class BaseTest(unittest.TestCase):
    def setUp(self):

        last_id = Meetups[-1]["id"]
        inc_id = last_id+1

        last_id = Questions[-1]["id"]
        qinc_id = last_id+1

        last_id = Rsvps[-1]["id"]
        rinc_id = last_id+1

        last_id = Comments[-1]["id"]
        cinc_id = last_id+1

        last_id = Users[-1]["id"]
        uinc_id = last_id+1

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

        self.data3 ={
            "id":rinc_id,
            "user": "Adam Cole",
            "responce": "Maybe",
        }

        self.data4 = {
            "id":cinc_id,
            "user":"Adam Cole",
            "responce":"You love it!"
        }

        self.data5 = {
            "id": uinc_id,
            "name": "Adam cole",
            "email": "adam@nxt",
            "username": "BayBay",
            "password": "undisputed4eva",
            "registered": "13/1/2019",
            "isAdmin": False
        }

        self.data6 = {
            "username": "BayBay",
            "password": "undisputed4eva"
        }

        self.data7 = {
            "id": inc_id,
            "createdOn": "",
            "location": "",
            "happeningOn": "",
            "topic": "",
            "Tags": "5w",
        }

        self.data8 = {
            "id": qinc_id,
            "createdOn": "",
            "createdBy": "",
            "meetup": 1,
            "title": "",
            "body": "",
            "votes": 0,
        }

        self.data9 = {
            "id": cinc_id,
            "user": "",
            "responce": ""
        }

        self.data10 = {
            "id": rinc_id,
            "user": "",
            "responce": "",
        }

        self.data11 = {
            "id": uinc_id,
            "name": "",
            "email": "adam@nxt",
            "username": "",
            "password": "undisputed4eva",
            "registered": "13/1/2019",
            "isAdmin": False
        }

        self.data12 = {
            "username": "BayBay",
            "password": ""
        }

class Test(BaseTest):
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

    def test_create_comment(self):
        for entry in Questions:
            i = entry["id"]
            qstn = entry["title"]
            response = self.client.post('questions/{}/comment'.format(i), data=json.dumps(self.data4), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))
            self.data4.update(question = qstn)

            assert response.status_code == 201
            assert data['status'] == 201
            assert data['data'] == [self.data4]

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

        j = Meetups[-1]["id"]+1

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

            response = self.client.post('/meetups/{}/rsvp'.format(i), data=json.dumps(self.data3),content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            
            assert response.status_code == 200
            #assert data['status'] == 200
            #assert data['data'] == [{"topic":topic,"meetup":i,"responce":self.data3["responce"]}]

    def test_signup(self):
        response = self.client.post('/signup', data=json.dumps(self.data5), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 201
        assert data['status'] == 201
        assert data['data'] == [self.data5]

    def test_signin(self):
        response = self.client.post('/signin', data=json.dumps(self.data6), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        #assert data['status'] == 200
        #assert data['data'] == ['{} logged in successfully'.format(self.data6["username"])]

class Test_empty(BaseTest):
    def test_create_meetup(self):
        response = self.client.post('/meetups', data=json.dumps(self.data7), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "One of more fields are empty"

    def test_create_question(self):
        response = self.client.post('/questions', data=json.dumps(self.data8), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "One of more fields are empty"

    def test_create_comment(self):
        for entry in Questions:
            i = entry["id"]
            qstn = entry["title"]
            response = self.client.post('questions/{}/comment'.format(i), data=json.dumps(self.data9), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))
            self.data4.update(question=qstn)

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "One of more fields are empty"

    def test_rsvp(self):
        for entry in Meetups:
            i = entry["id"]

            response = self.client.post('/meetups/{}/rsvp'.format(i), data=json.dumps(self.data10), content_type='application/json',)

            data = json.loads(response.get_data(as_text=True))

            assert response.status_code == 400
            assert data['status'] == 400
            assert data['error'] == "One of more fields are empty"

    def test_signup(self):
        response = self.client.post('/signup', data=json.dumps(self.data11), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "One of more fields are empty"

    def test_signin(self):

        response = self.client.post('/signin', data=json.dumps(self.data12), content_type='application/json',)

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 400
        assert data['status'] == 400
        assert data['error'] == "One of more fields are empty"



        

