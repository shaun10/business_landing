from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from flask_mail import Mail, Message
import datetime

#from database_setup import Base, MessageItem
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker



# engine = create_engine('sqlite:///contacts.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()

'''
1. Mock up
2. Routing can navigate to all the urls even if the pages are not yet completed
3. Templates and Forms, and proper functionality, want to see the templates rendering in application
4. CRUD Functionality, Create Read Update Delete
5. API Endpoints, calls to browser are working alright.
6. Styling and Message Flashing, CSS and Javascript incorporation
Clear deliverable at the end of the iteration
Main index updates
'''

app = Flask(__name__)
mail = Mail(app)
today = datetime.date

app.secret_key = 'sdh_attempt_at_anonymity'



#First line is used for the main site url
#useful for routing multiple urls to one place
#specifying type
@app.route('/')
def mainPage():
	return render_template('spa_temp.html')

	#flask allows us to render template instead of having to type line after line 
	#of these output updates. Old way is below before there were rendered templates

if __name__ == '__main__':
	#Needs to be more secure for real project 
	#Will reload the page without having to restart the server, useful
	app.debug = True
	#With framework response messages are simplified has a significant impact on code reduction
	app.run(host = '0.0.0.0', port = 5000)
	#app.run(host='0.0.0.0',debug=True)
	#app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
