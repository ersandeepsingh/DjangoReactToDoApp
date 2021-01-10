from django.urls import path

from .views import TaskView,BucketView,TaskDetailView,BucketDetailView

app_name = "ToDo"


urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>',TaskDetailView.as_view()),
    path('buckets/', BucketView.as_view()),
    path('buckets/<int:pk>',BucketDetailView.as_view()),
]