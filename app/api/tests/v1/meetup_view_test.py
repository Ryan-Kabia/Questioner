from v1.models.models import Meetup
from v1.views.meetup_view import app
from flask import json

data1 = {
    "id": 2,
    "createdOn": "12/1/2019",
    "location": "Hilton Park",
    "happeningOn": "31/2/2019",
    "topic": "wait that dont...",
    "Tags": ["prank", "fools"]
}


def test_create_meetup():
    response = app.test_client().post('/meetup',data = json.dumps(data1),content_type='application/json',)

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 201
    assert data['status'] == 201
    assert data['data'] == [data1]
