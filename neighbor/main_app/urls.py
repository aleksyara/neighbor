from django.urls import path 
# . import everything
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('jobposts/', views.jobposts_index, name='index'), 
    path('jobposts/<int:jobpost_id>/', views.jobposts_detail, name='detail'),
    path('jobposts/create/', views.JobPostCreate.as_view(), name='jobposts_create'), #handle GET & POST 
    path('jobposts<int:pk>/update/', views.JobPostUpdate.as_view(), name='jobposts_update'),
    path('jobposts/<int:pk>/delete/', views.JobPostDelete.as_view(), name='jobposts_delete'),
    path('jobposts/<int:jobpost_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    path('jobposts/<int:jobpost_id>/add-application/', views.jobposts_add_application, name='jobposts_add_application'),
    path('job-application/', views.job_application_create, name='job_application_create'),
    # path('volunteer/', views.volunteer_index, name='volunteer_index'),
    # path('profile/', views.profile, name='profile'),
]