from settings import app, api
from resources.UserProfile import UserProfileList, UserProfileDetail


# routes
api.add_resource(UserProfileList, '/service/api/userprofile')
api.add_resource(UserProfileDetail, '/service/api/userprofile/<id>')


# entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
