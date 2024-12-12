from app import routes
from server import Server
from state import state


server = Server(routes)
server.run()
