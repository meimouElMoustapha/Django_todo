from django.urls import path
from .views import home 
from .views import ModelNameDetail,postCreate,about,editview,DeletePostView
from Post.views import mainpage
from django.contrib.auth import  login,logout

#NoteList,NoteDetail,
from . import views
urlpatterns = [
    path('',mainpage,name="main1"),
    path('accounts/login',login,name="login"),
    path('accounts/logout',logout,name="logout"),
    
    path('create',views.postCreate.as_view(),name="create"),
    path('about',views.about,name="about"),
    # path('login/',loginview,name="login"),
    # path('logout/',logout_view,name="logout"),
    # path('register/',register_view,name="register"),
    path('home/',home,name="home"),
    path('detail/<pk>/',ModelNameDetail.as_view(),name="detail"),
   
    path('edit/<int:pk>/', editview.as_view(),name="edit"),
    path('delete/<int:id>/', DeletePostView.as_view(),name="delete"),
]







#   path('api', views.NoteList.as_view()),
#     path('<pk>/', views.NoteDetail.as_view()),
