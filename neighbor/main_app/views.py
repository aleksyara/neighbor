from django.shortcuts import render, redirect
from .models import JobPost

# Add the two imports below for Login New User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ""
  if request.method == "POST":
    #then we want to create user form object that includes the data from the browser
    form = UserCreationForm(request.POST) # < - object saved in memory
    if form.is_valid():
      # save user to DB
      user = form.save()
      # login our user (coming from auth)
      login(request, user) # <- this will create session cookie with sent back n forth on every request
      #redirect the user to the index
      return redirect('index') # index is coming frm name urls.py
    else: 
      error_message = 'Invalid sign up - try again'

  # A bad POST or a GET request, we'll render signup.html with an empty form 
  form = UserCreationForm()
  #^ this gives us the Blank Form
  context = {'form': form, 'error_message': error_message} # we injectin form and error to our html page
  return render(request, 'registration/signup.html', context) 

def home(request):
  return render(request, 'home.html') 

  # Define the ABOUT/ view
# def about(request):
#   return HttpResponse('<h1>This is About Page</h1>') # simmiluar to res.send

def about(request):
    return render(request, 'about.html') #instead of HTTPResponse we can use a template

  # A bad POST or a GET request, we'll render signup.html with an empty form 


# def posts_detail(request, post_id):
#   post = JobPost.objects.get(id=post_id)
#   return render(request, 'posts/detail.html', { 'post': post }) 

class JobPostUpdate(LoginRequiredMixin, UpdateView): 
  model = JobPost
  fields = ['description', 'date', 'maxPeople', 'compensation'] 

class JobPostDelete(LoginRequiredMixin, DeleteView):
  model = JobPost
  success_url = '/jobposts/'


class JobPostCreate(LoginRequiredMixin, CreateView):
  model = JobPost
  fields = ['name', 'description', 'date', 'maxPeople', 'compensation']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the job post. We're overriding the CreateView's form_valid method to assign the logged in user,
    # Let the CreateView do its job as usual
    return super().form_valid(form)


def jobposts_index(request):
  jobposts = JobPost.objects.all() 
  return render(request, 'jobposts/index.html', { 'jobposts': jobposts})


def jobposts_detail(request, jobpost_id):
  jobpost = JobPost.objects.get(id=jobpost_id)
  return render(request, 'jobposts/detail.html', {'jobpost': jobpost})
