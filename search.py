import os
import urllib
import cgi
import jinja2
import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SearchPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render())  

application = webapp2.WSGIApplication([
    ('/search', SearchPage),
], debug=True)     