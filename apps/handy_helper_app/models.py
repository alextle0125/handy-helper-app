from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self, post_data):
		errors = {}

		if len(post_data['f_name']) < 2:
			errors['f_name'] = "First name should be at least 2 characters"
		if len(post_data['l_name']) < 2:
			errors['l_name'] = "Last name should be at least 2 characters"
		if not EMAIL_REGEX.match(post_data['email']):
			errors['email'] = "Email is not a valid email address"
		if User.objects.filter(email=post_data['email']).count() == 1:
			errors['email'] = "Email has already been registered"
		if len(post_data['password']) < 8:
			errors['password'] = "Password must be at least 8 characters long"
		if post_data['password'] != post_data['confirm_password']:
			errors['confirm_password'] = "Password and confirmation password must match"

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class JobManager(models.Manager):
	def basic_validator(self, post_data):
		errors = {}

		if len(post_data['title']) < 4:
			errors['title'] = "Title should be at least 4 characters"
		if len(post_data['description']) < 10:
			errors['l_name'] = "Description should be at least 11 characters"
		if len(post_data['location']) < 1:
			errors['location'] = "Location must not be blank"

		return errors

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	location = models.CharField(max_length=255)
	completed = models.BooleanField(default=False)
	users = models.ManyToManyField(User, related_name="jobs")
	author_id = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = JobManager()
