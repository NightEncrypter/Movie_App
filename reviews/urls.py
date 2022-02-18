from django.urls import path
from . import views


urlpatterns=[
    # path("<str:review_id>",views.index,name="review"),
    # path("login",views.loginFunc,name="login2"),
    path("review",views.reviewForm,name="review_submit"),
]