from django.urls import path,include
from .import views
from .views import *
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path("user_register/",UserRegisterList.as_view(),name="userregister_list"),
    # path("user_register/<uuid:pk>/",UserRegisterDetails.as_view(),name="userregister_details")

]
