from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('courses',views.courses),
    path('courses/confirm/<int:course_id>',views.confirm),
    path('courses/destroy/<int:course_id>', views.destroy),
]