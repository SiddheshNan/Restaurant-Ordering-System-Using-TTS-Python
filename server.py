from tornado import websocket, web, ioloop, gen
import json
import asyncio
import threading
import tornado.ioloop
import tornado.web
import tornado.autoreload
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
            # message = json.dumps(message)
            c.write_message(message)

    def on_close(self):
        if self in cl:
            cl.remove(self)


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("gui.html")


class DebugHandler(web.RequestHandler):
    def get(self):
        self.render("debug.html")


app = web.Application([
    (r'/ws', SocketHandler),
    (r'/index', IndexHandler),
    (r'/debug', DebugHandler),
    (r'/static/(.*)', web.StaticFileHandler, {'path': './static/'}),
    (r'/(OrderLists.txt)', web.StaticFileHandler, {'path': './'})
])


def startServ():
    print("trying to start tornado server")
    app.listen(8888)
    tornado.autoreload.start()
    tornado.autoreload.watch('OrderLists.txt')
    ioloop.IOLoop.instance().start()


class WebServer(threading.Thread):
    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        app = web.Application([
            (r'/ws', SocketHandler),
            (r'/index', IndexHandler),
            (r'/debug', DebugHandler),
            (r'/static/(.*)', web.StaticFileHandler, {'path': './static/'}),
            (r'/(OrderLists.txt)', web.StaticFileHandler, {'path': './'})

        ])
        print("trying to start tornado server from threading")
        app.listen(8888)
        tornado.autoreload.start()
        tornado.autoreload.watch('OrderLists.txt')
        tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    startServ()
