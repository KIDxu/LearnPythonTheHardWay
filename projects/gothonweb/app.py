import web
import os

urls = (
    '/', 'Index'
)



render = web.template.render('/Users/jamie/Documents/Study/LearnPythonTheHardWay/ojects/gothonweb/templates/')
#render = web.template.render('/Users/jamie/Documents/Study/LearnPythonTheHardWay/ojects/gothonweb/templates/')
#render = web.template.render('templates/')

class Index(object):
    def GET(self):
#        return 'Hello World'
        greeting = 'Hello jon'
        return render.index(greeting=greeting)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# import web
# urls = (
#     '/','index'
# )
#
# app = web.application(urls, globals())
#
# class index:
#     def GET(self):
#         greeting = "Hello World"
#         return greeting
#
# if __name__ == "__main__":
#     app.run()
