from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def intro(request):
    
    return JsonResponse({'slackusername':'fish', 'backend':True, 'age': 25, 
    'bio': 'i am a backend intern at HNG internship program'})
