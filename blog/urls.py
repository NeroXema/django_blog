from django.urls import path
from blog import views
urlpatterns = [
    path('create/',views.post_create),
    path("", views.post_list),
    path('detail/<int:post_id>/',views.post_detail),
    path('update/<int:post_id>/',views.post_update),
    path('delete/<int:post_id>/',views.post_delete),
    ]