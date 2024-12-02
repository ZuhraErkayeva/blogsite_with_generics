from django.urls import path
from api.views import InstructorListCreateAPIView, InstructorRetrieveUpdateDestroyAPIView, CourseListCreateAPIView, \
    CourseRetrieveUpdateDestroyAPIView, LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('instructor/',InstructorListCreateAPIView.as_view()),
    path('instructor/<int:pk>/',InstructorRetrieveUpdateDestroyAPIView.as_view()),
    path('course/',CourseListCreateAPIView.as_view()),
    path('course/<int:pk>/',CourseRetrieveUpdateDestroyAPIView.as_view()),
    path('lesson/', LessonListCreateAPIView.as_view()),
    path('lesson/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view()),
]