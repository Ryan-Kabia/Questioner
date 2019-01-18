from datetime import datetime
from flask import json,jsonify

Users = []		

Meetups = []

Questions = []

Comments = []

Rsvps = []


class Meetup:

	def __init__(self, location, happeningOn, topic, tags):
		"""
		A class that creates a new meetup
		"""

		self.meetup_new = dict (
		id = (len(Meetups)+1),
		createdOn = datetime.utcnow().strftime("%d/%m/%Y"),
		location = location,
		happeningOn = happeningOn,
		topic = topic,
		Tags = tags,
		)
		self.meetups = Meetups
		
	def post_meetup(self):
		"""
		Class that post(saves) the created meetup to the database
		"""
		Meetups.append(self.meetup_new)
		return self.meetup_new

	def get_meetup(self):
		"""
		Class that displays all meetups in database
		"""
		return self.meetups

	def get_specific_meetup(self,meetup_id):
		"""
		Class that displays specific meetup in database
		"""
		for meetup in self.meetups:
			if meetup.get("id") == meetup_id:
				return meetup

		return False


class Question:
	def __init__(self,createdBy,meetup,title, body):
		"""
		Class to create a new question to be stored  in database
		"""

		self.question_new = dict (
		id = (len(Questions)+1),
		createdOn = datetime.utcnow().strftime("%d/%m/%Y"),
		createdBy = createdBy,
		meetup = meetup,
		title = title,
		body = body,
		votes = 0
		)

	def post_question(self):
		"""
		Class to post created question to database
		"""
		Questions.append(self.question_new)
		return self.question_new


class Comment:
	def __init__(self,user,responce,question):
		"""
		Class to create a new question to be stored  in database
		"""
		
		self.comment_new = dict (
		id = (len(Comments)+1),
		question = question,
		user = user,
		responce = responce,
		votes = 0
		)

		# if not self.comment_new.get("question"):
		# 	

	def post_comment(self):
		"""
		Class to post created question to database
		"""
		Comments.append(self.comment_new)
		return self.comment_new



class Rsvp:
	def __init__(self, id, meetup, user, responce):
		"""
		Class to create new rsvp entry
		"""
	
		self.id = id
		self.meetup = meetup
		self.user = user
		self.responce = responce

	def post_rsvp(self):
		Meetups.append(self)
