from django.shortcuts import render

# Create your views here for each link
# Each function would run a link

# This loads the /home page or root page
def home(request):
    return render(request, 'jobs/home.html')
