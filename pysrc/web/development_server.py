import os

import tornado.ioloop
import tornado.web

import sys

if sys.platform == 'win32':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


root = os.path.dirname(__file__)

cont = os.path.join(root, '../../deploy')
print(cont)

handlers = [
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": cont, 'default_filename': 'index.html'})
]

app = tornado.web.Application(handlers)
app.listen(8080)
tornado.ioloop.IOLoop.current().start()
