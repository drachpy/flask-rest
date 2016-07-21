from settings import app, api
from resources.UserProfile import UserProfileList, UserProfileDetail
from resources.Book import BookList, BookDetail


# routes
api.add_resource(UserProfileList, '/service/api/userprofile')
api.add_resource(UserProfileDetail, '/service/api/userprofile/<id>')
api.add_resource(BookList, '/service/api/book')
api.add_resource(BookDetail, '/service/api/book/<id>')


# entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
