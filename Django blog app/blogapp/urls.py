from django.urls import path, include
# from django.views.defaults import page_not_found
from . import views

urlpatterns = [
    path("", views.Homepage.as_view(), name="blog-home"),           # HOMEPAGE LINK 1
    # path("", views.home, name="blog-home"),
    path("home/", views.home, name="blog-homepage"),                # HOMEPAGE LINK 2
    path("about/", views.about, name="blog-about"),                 # ABOUT PAGE
    path("my-posts/", views.userpost, name="blog-post"),            # FOR THE LOGGED IN USER TO VIEW HIS OWN POSTS
    path("<str:name>/profileno_<int:pk>/", views.ViewUserProfile.as_view(), name='blog-profile'), #TO VIEW OTHER USERS PROFILE

    path("userpost/<str:username>/", views.UserPostListView.as_view(), name='user-post'), #TO VIEW POSTS OF ANY USER INCLUDING YOURSELF

    path("post/<int:pk>/details", views.PostDetail.as_view(), name='post-detail'),      # TO VIEW FULL DETAILS ABOUT ANY POST
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name='post-update'),  # TO UPDATE THE CONTENT OF ANY OF YOUR POST(LOGGED-IN USER)
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post-delete'),  # TO DELETE A POST THAT WAS CREATED BY THE LOGGED-IN USER
    path("post/new/", views.PostCreateView.as_view(), name='post-create'),              # FOR THE LOGGED IN USER TO CREATE A NEW POST OF HIS OR HER CHOICE
]