from settings import api

# routes
from resources.Ping import Ping
api.add_resource(Ping, '/service/api/ping')

from resources.UserProfile import UserProfileList, UserProfileDetail
api.add_resource(UserProfileList, '/service/api/userprofile')
api.add_resource(UserProfileDetail, '/service/api/userprofile/<id>')

from resources.Book import BookList, BookDetail
api.add_resource(BookList, '/service/api/book')
api.add_resource(BookDetail, '/service/api/book/<id>')
