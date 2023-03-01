from src import api, app, db
from src.createpost import CreatePost
from src.deletepost import DeletePost
from src.deleteuser import DeleteUser
from src.follow import Follow
from src.followuser import FollowUser
from src.home import Home
from src.index import Index
from src.login import Login
from src.profile import Profile
from src.logout import Logout
from src.search import Search
from src.signup import Signup
from src.unfollowuser import UnFollowUser
from src.updatepost import UpdatePost
from src.updateuser import UpdateUser
from src.viewpost import ViewPost
from src.viewposts import ViewPosts

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
