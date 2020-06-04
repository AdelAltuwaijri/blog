from django.urls import path
from . import views

urlpatterns=[
path('', views.home,name='home'),
path('about/',views.about,name="about"),
path('latest_posts/',views.home,name="latest"),
path('latest_comments/',views.home,name="latest"),
path('detail/<int:post_id>/',views.details,name="detail"),
path('new_post/',views.PostCreateView.as_view(),name="new_post"),
path('detail/<slug:pk>/update/',views.PostUpdateView.as_view(),name="post-update"),
path('detail/<slug:pk>/delete',views.PostDeleteView.as_view(),name="post-delete"),
]