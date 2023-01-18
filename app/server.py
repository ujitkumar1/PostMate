from app import api, app, db
from createpost import CreatePost
from deletepost import DeletePost
from deleteuser import DeleteUser
from follow import Follow
from followuser import FollowUser
from home import Home
from index import Index
from login import Login
from profile import Profile
from logout import Logout
from search import Search
from signup import Signup
from unfollowuser import UnFollowUser
from updatepost import UpdatePost
from updateuser import UpdateUser
from viewpost import ViewPost
from viewposts import ViewPosts

api.add_resource(Index, "/")
api.add_resource(Login, "/login")
api.add_resource(Follow, "/follow/<string:username>")
api.add_resource(Home, "/home")
api.add_resource(Search, "/search")
api.add_resource(Logout, "/logout")
api.add_resource(CreatePost, "/createpost")
api.add_resource(ViewPost, "/viewpost/<int:post_id>")
api.add_resource(ViewPosts, "/viewposts")
api.add_resource(UpdatePost, "/updatepost/<int:post_id>")
api.add_resource(DeletePost, "/deletepost/<int:post_id>")
api.add_resource(FollowUser, "/follow_user/<string:username>")
api.add_resource(UnFollowUser, '/unfollow_user/<string:username>')
api.add_resource(Signup, "/signup")
api.add_resource(Profile, "/profile/<string:username>")
api.add_resource(UpdateUser, "/updateuser/<int:user_id>")
api.add_resource(DeleteUser, "/deleteuser/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
