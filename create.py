import os
import urllib
import cgi
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_STREAMLIST_NAME = 'default_streamlist'


class CreatePage(webapp2.RequestHandler):

    def get(self):
        streamlist_name = self.request.get('streamlist_name',
                                          DEFAULT_STREAMLIST_NAME)
        template = JINJA_ENVIRONMENT.get_template('create.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
    ('/', CreatePage),
    ('/create', CreatePage)
    ], debug=True)              