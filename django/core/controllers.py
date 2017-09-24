from django.shortcuts import render

def index_controller(request):
    return render(request, 'core/index.html', {})
