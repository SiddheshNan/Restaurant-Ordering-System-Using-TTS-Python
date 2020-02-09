from tornado import websocket, web, ioloop
import json
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

cl = []


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_message(self, message):
        print(message)
        for c in cl:
            #message = json.dumps(message)
            c.write_message(message)

    def on_close(self):
        if self in cl:
            cl.remove(self)


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


app = web.Application([
    (r'/ws', SocketHandler),
    (r'/index', IndexHandler)
    #   (r'/css/(.*)', web.StaticFileHandler, {'path': './static/css'}),
    #   (r'/js/(.*)', web.StaticFileHandler, {'path': './static/js'}),
    #   (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    #   (r'/(rest_api_example.png)', web.StaticFileHandler, {'path': './static'}),
    #   (r'/(css.css)', web.StaticFileHandler, {'path': './templates'})
])


def startServ():
    print("trying to start tornado server")
    app.listen(8888)
    ioloop.IOLoop.instance().start()
