import tornado.ioloop
import tornado.web
from tornado.web import HTTPError

class PingHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('pong')

class ForwardHandler(tornado.web.RequestHandler):
	def get(self): 
		self.redirect('http://0.corslabs.com/html/0-0')

class HtmlHandler(tornado.web.RequestHandler):
    def get(self, sD = 0, rD = 0, suffix=''):
    	if suffix != '':
    		suffix = 'Cors' + suffix
    	self.render('static/template.html', scriptDomain=sD, restDomain=rD, suffix=suffix)

class ScriptHandler(tornado.web.RequestHandler):
    def get(self, rD, suffix):
    	self.set_header('Content-Type','text/javascript')
    	self.render('static/script.js', restDomain=rD, suffix=suffix)

class EchoHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(self.request.arguments)

	def post(self): 
		self.write(self.request.body)

class CorsAllEchoHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.write(self.request.arguments)

	def post(self): 
		self.set_header("Access-Control-Allow-Origin", "*")
		self.write(self.request.body)

class CorsSpecEchoHandler(tornado.web.RequestHandler):
	def get(self, id=''):
		self.set_header("Access-Control-Allow-Origin", "http://"+id+".corslabs.com")
		self.write(self.request.arguments)

	def post(self, id=''): 
		self.set_header("Access-Control-Allow-Origin", "http://"+id+".corslabs.com")
		self.write(self.request.body)

backend = tornado.web.Application([
    (r"/ping", PingHandler),
    (r"/", ForwardHandler),
    (r"/html/(\d*)-(\d*)-?(.*)", HtmlHandler),
    (r"/script(\d*)(.*).js", ScriptHandler),
    (r"/echo", EchoHandler),
    (r"/echoCorsAll", CorsAllEchoHandler),
    (r"/echoCors(\d*)", CorsSpecEchoHandler),
])

if __name__ == "__main__":
    backend.listen(2048)
    tornado.ioloop.IOLoop.instance().start()
    