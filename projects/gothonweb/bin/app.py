import web
urls = (
    '/', 'Index'
)
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting='Hello World'
        return render.index(greeting = greeting)
        #return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
