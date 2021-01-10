from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView


# Create your views here.
from .models import Bucket,Task
from .serializers import BucketSerializer,TaskSerializer



class BucketView(ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

class BucketDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

class TaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
