from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from apps.handy_helper_app.models import *

def index(request):
	if request.session.get('user_id'):
		user = User.objects.get(id=request.session['user_id'])

		context = {
			'user': user,
			'jobs': Job.objects.all(),
			'my_jobs': user.jobs.all()
		}

		return render(request, "handy_helper_app/index.html", context)
	else:
		return render(request, "handy_helper_app/login.html")

def create_user(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)

		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)

			return redirect("/")
		else:
			user = User.objects.create(first_name=request.POST['f_name'],last_name=request.POST['l_name'],email=request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))

			request.session['user_id'] = user.id

			return redirect("/")

def create_session(request):
	if request.method == "POST":
		user = User.objects.get(email=request.POST['email'])
		if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
			request.session['user_id'] = user.id

		return redirect("/")

def destroy_session(request):
	request.session.clear()

	return redirect("/")	

def new_job(request):
	return render(request, "handy_helper_app/new.html")

def create_job(request):
	if request.method == "POST":
		errors = Job.objects.basic_validator(request.POST)

		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)

			return redirect("/jobs/new")
		else:
			Job.objects.create(title=request.POST['title'],description=request.POST['description'],location=request.POST['location'],author_id=request.session['user_id'])
			return redirect("/")

def show_job(request, id):
	job = Job.objects.get(id=id)

	content = {
		"job": job,
		"user": User.objects.get(id=job.author_id)
	}

	return render(request, "handy_helper_app/show.html", content)

def edit_job(request, id):
	content = {
		"job": Job.objects.get(id=id)
	}	
	return render(request, "handy_helper_app/edit.html", content)

def update_job(request, id):
	if request.method == "POST":
		errors = Job.objects.basic_validator(request.POST)

		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)	
				
			return redirect("/jobs/%s/edit" % (id))
		else:		
			job = Job.objects.get(id=id)

			if request.POST['title'] != job.title:
				job.title = request.POST['title']
			if request.POST['description'] != job.description:
				job.description = request.POST['description']
			if request.POST['location'] != job.location:
				job.location = request.POST['location']

			job.save()

			content = {
				"job": job
			}

			return redirect("/")

def delete_job(request, id):
	job = Job.objects.get(id=id)

	job.delete()

	return redirect("/")

def add_job_to_user(request, id):
	user = User.objects.get(id=request.session['user_id'])
	job = Job.objects.get(id=id)

	user.jobs.add(job)

	return redirect("/")

def remove_job_to_user(request, id):
	user = User.objects.get(id=request.session['user_id'])
	job = Job.objects.get(id=id)

	user.jobs.remove(job)
	job.delete()

	return redirect("/")
