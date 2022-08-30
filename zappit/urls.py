from django.contrib import admin
from django.urls import path, include
from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts', views.PostList.as_view()),
    # upvote url
    path('api/posts/<int:pk>/vote', views.VoteCreate.as_view()),
    # allow other created users to login to the admin page
    path('api-auth/', include('rest_framework.urls')),

    # delete a post url
    path('api/posts/<int:pk>/', views.PostRetrieveDestroyAPIView.as_view()),
]
