from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def new_course_validator(self,postData):
        errors = {}
        if len(postData['course_name'])< 5:
            errors['course_name'] = "Course Name must be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Description must be at least 15 characters"
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


