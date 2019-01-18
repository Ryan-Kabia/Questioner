[![Build Status](https://travis-ci.org/Ryan-Kabia/Questioner.svg?branch=develop)](https://travis-ci.org/Ryan-Kabia/Questioner)   [![Coverage Status](https://coveralls.io/repos/github/Ryan-Kabia/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/Ryan-Kabia/Questioner?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/435a872e73e87002819d/maintainability)](https://codeclimate.com/github/Ryan-Kabia/Questioner/maintainability)
[![codecov](https://codecov.io/gh/Ryan-Kabia/Questioner/branch/develop/graph/badge.svg)](https://codecov.io/gh/Ryan-Kabia/Questioner)

### Getting Started

Questioner is a site that allows admin users to post meetups and crowd-source questions
which based by their number of upvotes, are prioritized to be answered.  

#### Features
* admin can create meetups
* users can post questions to meetups
* users can comment on questions posted
* users can upvote/downvote a question
* users can rsvp to a meetup

#### Prerequisites 
* Flask virtual Enviroment
* pip package installer
* Postman(for testing)
* Python 3.5.2

#### Heroku Hosting Link
* `ryanquestioner.herokuapp.com`

#### Endpoints

Endpoint       | Action       | Method |
------------- | ------------- | ---------------
/meetups/upcoming/ | retrieve all meetups | GET |
/meetups/<meetup_id> | retrieve specific meetup | GET |
/meetups | Post a new meetup | POST |
/questions | Post a new question | POST |
/questions/<question_id>/comment | Post a new comment | POST |
/meetups/<meetup_id>/rsvp | rsvp to specific meetup | POST |
/questions/<question_id>/upvote | upvote a question | PATCH |
/questions/<question_id>/downvote | downvote a question | PATCH |

#### Installation
* Clone the repo `https://github.com/Ryan-Kabia/Questioner` and navigate to the Question root Folder
* Setup up virtual enviroment using the `python3 -m venv myenv` command
* Activate virtual enviroment using `source myenv/bin/activate` command
* Install all requirments by running `pip install -r requirements.txt`
* set the Debug mode on using `export FLASK_DEBUG=1` command and also the development enviroment using `export FLASK_ENV=development` command and finally choose the run.py app to run using `export FLASK_APP=run.py`command
* run the application using `flask run` command

#### Running tests
* navigate to `Qustioner/app/api/tests/v1` and run `pytest meetup_view_test.py` command

#### Postman
* using the above endpoints with url generated by flask server and passing data in a JSON format where needed

#### Author
Ryan Kabia






