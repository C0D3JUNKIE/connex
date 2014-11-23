import os
import urllib
import cgi
import jinja2
import webapp2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

STREAMINFO = 'default_streaminfo'

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def streaminfo_key(streaminfo_name=STREAMINFO):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Stream Name', streaminfo_name)

class Streams(ndb.Model):
    """Models an individual Stream entry."""
    stream_name = ndb.StringProperty(indexed=False)
    thumb_img = ndb.BlobProperty()
    owner_name = ndb.UserProperty()
    stream_id = ndb.StringProperty(required=True, indexed=True)
    owner_name = ndb.StringProperty(indexed=False)
    subscriber_list = ndb.StringProperty(indexed=False)
    create_date = ndb.DateTimeProperty(auto_now_add=True)
    category_id = ndb.IntegerProperty(required=False, indexed=False)
    category_name = ndb.StringProperty()
    location_id = ndb.StringProperty()
    location_name = ndb.StringProperty()

class CreatePage(webapp2.RequestHandler):

    def get(self):
        stream_name = self.request.get('stream_name', STREAMINFO)
        thumb_img = self.request.get('thunmb_img', STREAMINFO)
        stream_id = self.request.get('stream_id', STREAMINFO)
        owner_name = self.request.get('owner_name', STREAMINFO)
        subscriber_list = self.request.get('subscriber_list', STREAMINFO)
        create_date = self.request.get('create_date', STREAMINFO)
        category_id = self.request.get('category_id', STREAMINFO)
        category_name = self.request.get('category_name', STREAMINFO)
        location_id = self.request.get('location_id', STREAMINFO)
        location_name = self.request.get('location_name', STREAMINFO)
        
        template = JINJA_ENVIRONMENT.get_template('create.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
    ('/', CreatePage),
    ('/create', CreatePage)
    ], debug=True)              