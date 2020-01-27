from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

@csrf_exempt
def index(request):
    msg = messages.get_messages(request)
    return render(request, "login.html", {'messages': msg})