Users = [{
		"id": 1,
		"name": "admin",
		"email": "admin@qstn",
		"username": "admin",
		"password": "admin123",
		"registered": "12/1/2019",
		"isAdmin":True
		}]		

Meetups = [{
        "id":1,
        "createdOn":"8/1/2019",
        "location":"Hilton Park",
        "happeningOn": "15/2/2019",
        "topic":"Not very lit fam!",
        "Tags":["lit,fam"],
        },{
        "id":2,
        "createdOn":"13/1/2019",
        "location":"baltimore Park",
        "happeningOn": "18/3/2019",
        "topic":"Not lit fam!",
        "Tags":["lit,fam"],
        },{
        "id":3,
        "createdOn":"18/1/2019",
        "location":"putin Park",
        "happeningOn": "14/3/2019",
        "topic":"lit fam!",
        "Tags":["lit,fam"],
        }]

Questions = [{
    "id": 1,
    "createdOn": "8/1/2019",
    "createdBy": "Adam Cole",
    "meetup": 1,
    "title": "but is it undisputed?",
    "body":"Hell nah, only the cfos run the place!!",
    "votes": 0,
        }]

Comments = [{
			"id": 1,
            "question": "but is it undisputed?",
            "user": "Kyle O'Riely",
            "responce": "Tapout 24/7"
			}]

Rsvps = [{
        "id":1,
        "meetup":1,
        "user":"Adam Cole",
        "responce":"yes"
        }]

class User:
	def __init__(self, id, name, email, username, password, registerd, isAdmin):

		self.id = id
		self.name = name
		self.email = email
		self.username = username
		self.password = password
		self.registerd = registerd
		self.isAdmin = isAdmin
	
	def save_user(self):
		Users.append(self)

	@staticmethod
	def del_user(user):
		Users.remove(user)


class Meetup:
	def __init__(self, id, createdOn, location, happeningOn, topic, tags):

		self.id = id
		self.createdOn = createdOn
		self.location = location
		self.happeningOn = happeningOn
		self.topic = topic
		self.tags = tags

	def save_meetup(self):
		Meetups.append(self)

	@staticmethod
	def del_meetup(meetup):
		Meetups.remove(meetup)


class Question:
	def __init__(self, id, createdOn, createdBy, happeningOn, title, body, votes):

		self.id = id
		self.createdOn = createdOn
		self.createdBy = createdBy
		self.happeningOn = happeningOn
		self.title = title
		self.body = body
		self.votes = votes


	def save_question(self):
		Meetups.append(self)

	@staticmethod
	def del_question(qstn):
		Meetups.remove(qstn)


class Rsvp:
	def __init__(self, id, meetup, user, responce):

		self.id = id
		self.meetup = meetup
		self.user = user
		self.responce = responce

	def save_rsvp(self):
		Meetups.append(self)

	@staticmethod
	def del_rsvp(rsvp):
		Meetups.remove(rsvp)
