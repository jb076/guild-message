from django.shortcuts import render

def index(request):
    cxt = {}
    user = request.user
    return render(request, 'index.html', cxt)
